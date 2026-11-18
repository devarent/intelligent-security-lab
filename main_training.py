"""
Main Training Script for Cyber Security ML Models
This script demonstrates training and evaluation of various ML models for cyber security threat detection
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# Import custom modules
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.feature_engineering import FeatureEngineer
from src.preprocessing.imbalance_handler import ImbalanceHandler
from src.preprocessing.data_splitter import DataSplitter
from src.models.isolation_forest_model import IsolationForestModel
from src.models.ensemble_model import EnsembleModel

print("=" * 80)
print("CYBER SECURITY ML TRAINING PIPELINE")
print("=" * 80)

# ============================================================================
# 1. DATA LOADING (Example with synthetic data for demonstration)
# ============================================================================
print("\n[1] Loading Data...")

# For demonstration, we'll create synthetic data
# In production, replace this with actual dataset loading
np.random.seed(42)
n_samples = 10000
n_features = 20

# Generate synthetic network traffic data
X = np.random.randn(n_samples, n_features)
y = np.random.choice([0, 1], size=n_samples, p=[0.8, 0.2])  # 80% normal, 20% attack

# Create feature names
feature_names = [f'feature_{i}' for i in range(n_features)]
df = pd.DataFrame(X, columns=feature_names)
df['label'] = y

print(f"Dataset shape: {df.shape}")
print(f"Class distribution:\n{df['label'].value_counts()}")

# ============================================================================
# 2. DATA CLEANING
# ============================================================================
print("\n[2] Data Cleaning...")

cleaner = DataCleaner()
df_cleaned = cleaner.clean_data(df)

print(f"Data shape after cleaning: {df_cleaned.shape}")

# ============================================================================
# 3. FEATURE ENGINEERING
# ============================================================================
print("\n[3] Feature Engineering...")

engineer = FeatureEngineer()

# Separate features and labels
X = df_cleaned.drop('label', axis=1)
y = df_cleaned['label']

# Normalize features
X_normalized = engineer.normalize_features(X, method='standard')

print(f"Features normalized: {X_normalized.shape}")

# ============================================================================
# 4. HANDLING CLASS IMBALANCE
# ============================================================================
print("\n[4] Handling Class Imbalance...")

imbalance_handler = ImbalanceHandler()

# Apply SMOTE to balance classes
X_resampled, y_resampled = imbalance_handler.apply_smote(X_normalized, y)

print(f"Data shape after SMOTE: {X_resampled.shape}")
print(f"Class distribution after SMOTE:\n{pd.Series(y_resampled).value_counts()}")

# ============================================================================
# 5. DATA SPLITTING
# ============================================================================
print("\n[5] Data Splitting...")

splitter = DataSplitter()
X_train, X_val, X_test, y_train, y_val, y_test = splitter.split_data(
    X_resampled, y_resampled, test_size=0.15, val_size=0.15, stratify=True
)

# ============================================================================
# 6. TRAINING ISOLATION FOREST MODEL
# ============================================================================
print("\n[6] Training Isolation Forest Model...")

iso_forest = IsolationForestModel(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Train on normal data only (unsupervised)
iso_forest.train(X_train[y_train == 0])

# Evaluate
print("\nEvaluating Isolation Forest...")
iso_forest.evaluate(X_test, y_test)

# Save model
iso_forest.save_model('data/models/isolation_forest.pkl')

# ============================================================================
# 7. TRAINING ENSEMBLE MODEL
# ============================================================================
print("\n[7] Training Ensemble Model...")

ensemble = EnsembleModel()
ensemble.build_base_models()

# Train base models
ensemble.train_base_models(X_train, y_train)

# Train meta model
ensemble.train_meta_model(X_train, y_train, X_val, y_val)

# Evaluate
print("\nEvaluating Ensemble Model...")
y_pred, y_pred_proba = ensemble.evaluate(X_test, y_test)

# Cross-validation
print("\nPerforming Cross-Validation...")
cv_scores = ensemble.cross_validate(X_resampled, y_resampled, cv=5)

# Save models
ensemble.save_models('data/models/ensemble')

# ============================================================================
# 8. SUMMARY
# ============================================================================
print("\n" + "=" * 80)
print("TRAINING SUMMARY")
print("=" * 80)
print("\nModels trained and saved:")
print("1. Isolation Forest: data/models/isolation_forest.pkl")
print("2. Ensemble Model: data/models/ensemble_*.pkl")
print("\nAll models are ready for deployment!")
print("=" * 80)

# ============================================================================
# 9. INFERENCE EXAMPLE
# ============================================================================
print("\n[8] Inference Example...")

# Load ensemble model
print("Loading ensemble model...")
ensemble.load_models('data/models/ensemble')

# Sample prediction
sample_data = X_test[:5]
predictions = ensemble.predict(sample_data)
probabilities = ensemble.predict_proba(sample_data)

print("\nSample Predictions:")
for i, (pred, prob) in enumerate(zip(predictions, probabilities)):
    print(f"Sample {i+1}: Predicted={pred}, Probability={prob}")

print("\n" + "=" * 80)
print("TRAINING PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 80)
