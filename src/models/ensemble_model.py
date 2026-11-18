"""
Ensemble Model using Stacking Method
Combines Random Forest, XGBoost, and LightGBM
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import xgboost as xgb
import lightgbm as lgb
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

class EnsembleModel:
    """Implementasi Ensemble Method dengan Stacking"""

    def __init__(self):
        self.rf_model = None
        self.xgb_model = None
        self.lgb_model = None
        self.meta_model = None
        self.base_models = []

    def build_base_models(self):
        """Bangun base models"""
        # Random Forest
        self.rf_model = RandomForestClassifier(
            n_estimators=200,
            max_depth=20,
            min_samples_split=5,
            class_weight='balanced',
            random_state=42,
            n_jobs=-1
        )

        # XGBoost
        self.xgb_model = xgb.XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            n_jobs=-1
        )

        # LightGBM
        self.lgb_model = lgb.LGBMClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            num_leaves=31,
            is_unbalance=True,
            random_state=42,
            n_jobs=-1,
            verbose=-1
        )

        self.base_models = [
            ('rf', self.rf_model),
            ('xgb', self.xgb_model),
            ('lgb', self.lgb_model)
        ]

        return self.base_models

    def train_base_models(self, X_train, y_train):
        """Latih base models"""
        print("Training base models...")

        for name, model in self.base_models:
            print(f"Training {name}...")
            model.fit(X_train, y_train)
            print(f"{name} training completed")

    def get_base_predictions(self, X, method='predict_proba'):
        """Dapatkan prediksi dari base models"""
        predictions = []

        for name, model in self.base_models:
            if method == 'predict_proba':
                pred = model.predict_proba(X)
            else:
                pred = model.predict(X).reshape(-1, 1)
            predictions.append(pred)

        return np.hstack(predictions)

    def train_meta_model(self, X_train, y_train, X_val, y_val):
        """Latih meta model dengan cross-validation"""
        print("Training meta model (Stacking)...")

        # Get predictions from base models on validation set
        meta_features = self.get_base_predictions(X_val, method='predict_proba')

        # Train meta model
        self.meta_model = LogisticRegression(
            C=1.0,
            max_iter=1000,
            random_state=42
        )
        self.meta_model.fit(meta_features, y_val)

        print("Meta model training completed")

    def predict(self, X):
        """Prediksi menggunakan ensemble"""
        # Get predictions from base models
        meta_features = self.get_base_predictions(X, method='predict_proba')

        # Predict using meta model
        return self.meta_model.predict(meta_features)

    def predict_proba(self, X):
        """Dapatkan probability predictions"""
        meta_features = self.get_base_predictions(X, method='predict_proba')
        return self.meta_model.predict_proba(meta_features)

    def evaluate(self, X_test, y_test):
        """Evaluasi ensemble model"""
        y_pred = self.predict(X_test)
        y_pred_proba = self.predict_proba(X_test)

        print("Classification Report:")
        print(classification_report(y_test, y_pred))

        print("Confusion Matrix:")
        cm = confusion_matrix(y_test, y_pred)
        print(cm)

        # Plot confusion matrix
        try:
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title('Confusion Matrix - Ensemble Model')
            plt.ylabel('True Label')
            plt.xlabel('Predicted Label')
            plt.savefig('confusion_matrix_ensemble.png')
            plt.close()
        except Exception as e:
            print(f"Could not save confusion matrix plot: {e}")
            pass

        # ROC-AUC
        if len(np.unique(y_test)) == 2:
            roc_auc = roc_auc_score(y_test, y_pred_proba[:, 1])
            print(f"ROC-AUC Score: {roc_auc:.4f}")

        return y_pred, y_pred_proba

    def cross_validate(self, X, y, cv=5):
        """Cross-validation untuk ensemble"""
        print(f"Performing {cv}-fold cross validation...")

        cv_scores = {}
        for name, model in self.base_models:
            scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy', n_jobs=-1)
            cv_scores[name] = scores
            print(f"{name} - Mean CV Accuracy: {scores.mean():.4f} (+/- {scores.std():.4f})")

        return cv_scores

    def save_models(self, path_prefix):
        """Simpan semua models"""
        joblib.dump(self.rf_model, f'{path_prefix}_rf.pkl')
        joblib.dump(self.xgb_model, f'{path_prefix}_xgb.pkl')
        joblib.dump(self.lgb_model, f'{path_prefix}_lgb.pkl')
        joblib.dump(self.meta_model, f'{path_prefix}_meta.pkl')
        print("All models saved")

    def load_models(self, path_prefix):
        """Load semua models"""
        self.rf_model = joblib.load(f'{path_prefix}_rf.pkl')
        self.xgb_model = joblib.load(f'{path_prefix}_xgb.pkl')
        self.lgb_model = joblib.load(f'{path_prefix}_lgb.pkl')
        self.meta_model = joblib.load(f'{path_prefix}_meta.pkl')

        self.base_models = [
            ('rf', self.rf_model),
            ('xgb', self.xgb_model),
            ('lgb', self.lgb_model)
        ]
        print("All models loaded")
