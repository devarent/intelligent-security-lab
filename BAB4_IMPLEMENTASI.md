# BAB IV
# IMPLEMENTASI

## 4.1 Lingkungan Pengembangan

### 4.1.1 Hardware

Pengembangan dan pelatihan model dilakukan pada sistem dengan spesifikasi berikut:

- **Processor**: Intel Core i7 atau AMD Ryzen 7 (16 threads)
- **RAM**: 32 GB DDR4
- **Storage**: SSD 1 TB NVMe
- **GPU**: NVIDIA RTX 3060/3080 (optional, untuk deep learning)

GPU digunakan untuk mempercepat pelatihan model deep learning (CNN, GCN, LLM) menggunakan CUDA. Jika GPU tidak tersedia, pelatihan dapat dilakukan menggunakan CPU namun dengan waktu yang lebih lama.

### 4.1.2 Software dan Operating System

- **Operating System**: Windows 10/11 atau Linux (Ubuntu 20.04/22.04)
- **Python Version**: 3.9 atau 3.10
- **Package Manager**: pip atau conda

### 4.1.3 Library dan Framework

Library Python yang digunakan dalam penelitian ini:

**Machine Learning dan Data Processing:**
```python
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
imbalanced-learn==0.11.0
xgboost==1.7.6
lightgbm==4.0.0
```

**Deep Learning:**
```python
tensorflow==2.13.0
torch==2.0.1
torchvision==0.15.2
keras==2.13.1
```

**Graph Neural Networks:**
```python
torch-geometric==2.3.1
```

**NLP dan LLM:**
```python
transformers==4.33.1
datasets==2.14.4
tokenizers==0.13.3
```

**Web Framework:**
```python
flask==2.3.2
flask-cors==4.0.0
```

**Visualization:**
```python
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.15.0
```

**Utility:**
```python
joblib==1.3.1
tqdm==4.65.0
```

### 4.1.4 Struktur Direktori Proyek

```
Keamanan Berbasis Sistem Cerdas/
├── data/
│   ├── raw/              # Dataset mentah
│   ├── processed/        # Dataset yang sudah dipreprocessing
│   └── models/           # Model yang sudah dilatih
├── notebooks/            # Jupyter notebooks untuk eksplorasi
├── src/
│   ├── preprocessing/    # Modul preprocessing
│   ├── models/           # Implementasi model
│   ├── utils/            # Utility functions
│   └── api/              # Backend API untuk dashboard
├── dashboard/            # Frontend dashboard
├── tests/                # Unit tests
├── docs/                 # Dokumentasi
├── requirements.txt      # Dependencies
├── README.md            # Dokumentasi proyek
└── config.yaml          # Konfigurasi
```

## 4.2 Implementasi Preprocessing Data

### 4.2.1 Data Loading

**File: `src/preprocessing/data_loader.py`**

```python
import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    """Class untuk loading dataset keamanan siber"""

    def __init__(self, data_dir='data/raw'):
        self.data_dir = Path(data_dir)

    def load_cic_ids2017(self, file_path):
        """Load dataset CIC-IDS2017"""
        df = pd.read_csv(self.data_dir / file_path)
        return df

    def load_cic_ids2018(self, file_path):
        """Load dataset CIC-IDS2018"""
        df = pd.read_csv(self.data_dir / file_path)
        return df

    def load_cic_ddos2019(self, file_path):
        """Load dataset CIC-DDoS2019"""
        df = pd.read_csv(self.data_dir / file_path)
        return df

    def load_iot_attack(self, file_path):
        """Load dataset IoT Attack"""
        df = pd.read_csv(self.data_dir / file_path)
        return df

    def load_malnet_images(self, image_dir):
        """Load dataset MalNet-Image"""
        from tensorflow.keras.preprocessing import image_dataset_from_directory
        dataset = image_dataset_from_directory(
            self.data_dir / image_dir,
            image_size=(64, 64),
            batch_size=32,
            label_mode='categorical'
        )
        return dataset

    def load_cyberllm_instruct(self, file_path):
        """Load dataset CyberLLMInstruct"""
        import json
        with open(self.data_dir / file_path, 'r') as f:
            data = json.load(f)
        return data
```

### 4.2.2 Data Cleaning

**File: `src/preprocessing/data_cleaner.py`**

```python
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

class DataCleaner:
    """Class untuk pembersihan data"""

    def __init__(self):
        pass

    def handle_missing_values(self, df, threshold=0.2):
        """Handle missing values berdasarkan threshold"""
        # Hapus kolom dengan missing values > threshold
        missing_ratio = df.isnull().sum() / len(df)
        cols_to_drop = missing_ratio[missing_ratio > threshold].index
        df = df.drop(columns=cols_to_drop)

        # Isi missing values untuk kolom numerik
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 0:
            imputer_num = SimpleImputer(strategy='median')
            df[numeric_cols] = imputer_num.fit_transform(df[numeric_cols])

        # Isi missing values untuk kolom kategorikal
        cat_cols = df.select_dtypes(include=['object']).columns
        if len(cat_cols) > 0:
            imputer_cat = SimpleImputer(strategy='most_frequent')
            df[cat_cols] = imputer_cat.fit_transform(df[cat_cols])

        return df

    def remove_duplicates(self, df):
        """Hapus baris duplikat"""
        initial_len = len(df)
        df = df.drop_duplicates()
        print(f"Removed {initial_len - len(df)} duplicate rows")
        return df

    def handle_outliers(self, df, method='iqr', threshold=3):
        """Handle outliers menggunakan IQR atau Z-score"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        for col in numeric_cols:
            if method == 'iqr':
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df[col] = df[col].clip(lower_bound, upper_bound)

            elif method == 'zscore':
                z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
                df.loc[z_scores > threshold, col] = df[col].median()

        return df

    def clean_data(self, df):
        """Pipeline pembersihan data lengkap"""
        print("Starting data cleaning...")
        df = self.handle_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.handle_outliers(df)
        print("Data cleaning completed")
        return df
```

### 4.2.3 Normalisasi dan Feature Engineering

**File: `src/preprocessing/feature_engineering.py`**

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.decomposition import PCA

class FeatureEngineer:
    """Class untuk feature engineering dan normalisasi"""

    def __init__(self):
        self.scaler = None
        self.label_encoders = {}

    def normalize_features(self, df, method='standard'):
        """Normalisasi fitur numerik"""
        numeric_cols = df.select_dtypes(include=[np.number]).columns

        if method == 'standard':
            self.scaler = StandardScaler()
        elif method == 'minmax':
            self.scaler = MinMaxScaler()

        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])
        return df

    def encode_categorical(self, df, method='onehot'):
        """Encode fitur kategorikal"""
        cat_cols = df.select_dtypes(include=['object']).columns

        if method == 'onehot':
            df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
        elif method == 'label':
            for col in cat_cols:
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                df[col] = self.label_encoders[col].fit_transform(df[col])

        return df

    def extract_time_features(self, df, timestamp_col):
        """Ekstrak fitur waktu dari timestamp"""
        df[timestamp_col] = pd.to_datetime(df[timestamp_col])

        df['hour'] = df[timestamp_col].dt.hour
        df['day_of_week'] = df[timestamp_col].dt.dayofweek
        df['day_of_month'] = df[timestamp_col].dt.day
        df['month'] = df[timestamp_col].dt.month

        # Cyclic encoding untuk hour dan day_of_week
        df['hour_sin'] = np.sin(2 * np.pi * df['hour'] / 24)
        df['hour_cos'] = np.cos(2 * np.pi * df['hour'] / 24)
        df['day_sin'] = np.sin(2 * np.pi * df['day_of_week'] / 7)
        df['day_cos'] = np.cos(2 * np.pi * df['day_of_week'] / 7)

        return df

    def create_ratio_features(self, df):
        """Buat fitur rasio"""
        # Contoh: ratio antara forward dan backward packets
        if 'Forward Packets' in df.columns and 'Backward Packets' in df.columns:
            df['fwd_bwd_packet_ratio'] = df['Forward Packets'] / (df['Backward Packets'] + 1)

        # Contoh: ratio antara total bytes dan packets
        if 'Total Bytes' in df.columns and 'Total Packets' in df.columns:
            df['bytes_per_packet'] = df['Total Bytes'] / (df['Total Packets'] + 1)

        return df

    def apply_pca(self, df, n_components=0.95):
        """Terapkan PCA untuk reduksi dimensi"""
        pca = PCA(n_components=n_components)
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        df_pca = pca.fit_transform(df[numeric_cols])

        # Buat dataframe baru dengan komponen PCA
        feature_names = [f'PC{i+1}' for i in range(df_pca.shape[1])]
        df_pca = pd.DataFrame(df_pca, columns=feature_names)

        print(f"PCA reduced dimensions from {len(numeric_cols)} to {df_pca.shape[1]}")
        print(f"Explained variance ratio: {pca.explained_variance_ratio_.sum():.4f}")

        return df_pca, pca
```

### 4.2.4 Handling Class Imbalance

**File: `src/preprocessing/imbalance_handler.py`**

```python
import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE, SMOTENC
from imblearn.combine import SMOTEENN
from imblearn.under_sampling import RandomUnderSampler
from collections import Counter

class ImbalanceHandler:
    """Class untuk menangani class imbalance"""

    def __init__(self):
        pass

    def apply_smote(self, X, y, sampling_strategy='auto', random_state=42):
        """Terapkan SMOTE untuk oversampling"""
        print(f"Original class distribution: {Counter(y)}")

        smote = SMOTE(sampling_strategy=sampling_strategy, random_state=random_state)
        X_resampled, y_resampled = smote.fit_resample(X, y)

        print(f"Resampled class distribution: {Counter(y_resampled)}")
        return X_resampled, y_resampled

    def apply_smote_enn(self, X, y, sampling_strategy='auto', random_state=42):
        """Terapkan SMOTE + ENN (hybrid method)"""
        print(f"Original class distribution: {Counter(y)}")

        smote_enn = SMOTEENN(sampling_strategy=sampling_strategy, random_state=random_state)
        X_resampled, y_resampled = smote_enn.fit_resample(X, y)

        print(f"Resampled class distribution: {Counter(y_resampled)}")
        return X_resampled, y_resampled

    def apply_undersampling(self, X, y, sampling_strategy='auto', random_state=42):
        """Terapkan random undersampling"""
        print(f"Original class distribution: {Counter(y)}")

        undersampler = RandomUnderSampler(sampling_strategy=sampling_strategy, random_state=random_state)
        X_resampled, y_resampled = undersampler.fit_resample(X, y)

        print(f"Resampled class distribution: {Counter(y_resampled)}")
        return X_resampled, y_resampled

    def get_class_weights(self, y):
        """Hitung class weights untuk use dalam model"""
        from sklearn.utils.class_weight import compute_class_weight
        classes = np.unique(y)
        weights = compute_class_weight('balanced', classes=classes, y=y)
        class_weights = dict(zip(classes, weights))
        return class_weights
```

### 4.2.5 Data Splitting

**File: `src/preprocessing/data_splitter.py`**

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.model_selection import TimeSeriesSplit

class DataSplitter:
    """Class untuk splitting data"""

    def __init__(self):
        pass

    def split_data(self, X, y, test_size=0.15, val_size=0.15, random_state=42, stratify=True):
        """Split data menjadi train, validation, dan test sets"""
        # Pertama, split train+val dan test
        if stratify:
            X_train_val, X_test, y_train_val, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state, stratify=y
            )
        else:
            X_train_val, X_test, y_train_val, y_test = train_test_split(
                X, y, test_size=test_size, random_state=random_state
            )

        # Kedua, split train dan validation dari train+val
        val_size_adjusted = val_size / (1 - test_size)
        if stratify:
            X_train, X_val, y_train, y_val = train_test_split(
                X_train_val, y_train_val, test_size=val_size_adjusted,
                random_state=random_state, stratify=y_train_val
            )
        else:
            X_train, X_val, y_train, y_val = train_test_split(
                X_train_val, y_train_val, test_size=val_size_adjusted,
                random_state=random_state
            )

        print(f"Train set size: {len(X_train)} ({len(X_train)/len(X)*100:.1f}%)")
        print(f"Validation set size: {len(X_val)} ({len(X_val)/len(X)*100:.1f}%)")
        print(f"Test set size: {len(X_test)} ({len(X_test)/len(X)*100:.1f}%)")

        return X_train, X_val, X_test, y_train, y_val, y_test

    def temporal_split(self, X, y, test_size=0.15, val_size=0.15):
        """Split data secara temporal untuk time series"""
        n = len(X)
        test_start = int(n * (1 - test_size))
        val_start = int(n * (1 - test_size - val_size))

        X_train, y_train = X[:val_start], y[:val_start]
        X_val, y_val = X[val_start:test_start], y[val_start:test_start]
        X_test, y_test = X[test_start:], y[test_start:]

        print(f"Train set size: {len(X_train)}")
        print(f"Validation set size: {len(X_val)}")
        print(f"Test set size: {len(X_test)}")

        return X_train, X_val, X_test, y_train, y_val, y_test

    def stratified_kfold(self, X, y, n_splits=5, random_state=42):
        """Stratified K-Fold cross validation"""
        skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=random_state)
        return skf.split(X, y)
```

## 4.3 Implementasi Model Isolation Forest

**File: `src/models/isolation_forest_model.py`**

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

class IsolationForestModel:
    """Implementasi Isolation Forest untuk deteksi anomali"""

    def __init__(self, n_estimators=100, contamination=0.1, random_state=42):
        self.n_estimators = n_estimators
        self.contamination = contamination
        self.random_state = random_state
        self.model = None

    def train(self, X_train):
        """Latih model Isolation Forest"""
        print("Training Isolation Forest...")
        self.model = IsolationForest(
            n_estimators=self.n_estimators,
            contamination=self.contamination,
            random_state=self.random_state,
            n_jobs=-1
        )
        self.model.fit(X_train)
        print("Training completed")

    def predict(self, X):
        """Prediksi anomali (-1 untuk anomali, 1 untuk normal)"""
        return self.model.predict(X)

    def predict_anomaly_score(self, X):
        """Dapatkan anomaly score (semakin rendah = semakin anomali)"""
        return self.model.score_samples(X)

    def evaluate(self, X_test, y_test):
        """Evaluasi model"""
        y_pred = self.predict(X_test)
        # Convert: -1 (anomali) -> 1, 1 (normal) -> 0
        y_pred_binary = np.where(y_pred == -1, 1, 0)

        print("Classification Report:")
        print(classification_report(y_test, y_pred_binary))

        print("Confusion Matrix:")
        cm = confusion_matrix(y_test, y_pred_binary)
        print(cm)

        # Plot confusion matrix
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix - Isolation Forest')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig('confusion_matrix_isolation_forest.png')
        plt.close()

        return y_pred_binary

    def save_model(self, path):
        """Simpan model ke disk"""
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")

    def load_model(self, path):
        """Load model dari disk"""
        self.model = joblib.load(path)
        print(f"Model loaded from {path}")
```

## 4.4 Implementasi Model CNN

**File: `src/models/cnn_model.py`**

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

class CNNModel:
    """Implementasi CNN untuk klasifikasi malware berbasis citra"""

    def __init__(self, input_shape=(64, 64, 3), num_classes=None):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = None

    def build_model(self):
        """Bangun arsitektur CNN"""
        model = keras.Sequential([
            # Block 1
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            layers.MaxPooling2D((2, 2)),
            layers.BatchNormalization(),
            layers.Dropout(0.25),

            # Block 2
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.BatchNormalization(),
            layers.Dropout(0.25),

            # Block 3
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.BatchNormalization(),
            layers.Dropout(0.25),

            # Flatten
            layers.Flatten(),

            # Dense layers
            layers.Dense(256, activation='relu'),
            layers.BatchNormalization(),
            layers.Dropout(0.5),

            # Output layer
            layers.Dense(self.num_classes, activation='softmax')
        ])

        model.compile(
            optimizer=keras.optimizers.Adam(learning_rate=0.001),
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

        self.model = model
        model.summary()
        return model

    def train(self, train_dataset, val_dataset, epochs=50, batch_size=32):
        """Latih model CNN"""
        print("Training CNN model...")

        # Callbacks
        early_stopping = EarlyStopping(
            monitor='val_loss',
            patience=10,
            restore_best_weights=True
        )

        model_checkpoint = ModelCheckpoint(
            'best_cnn_model.h5',
            monitor='val_accuracy',
            save_best_only=True
        )

        reduce_lr = ReduceLROnPlateau(
            monitor='val_loss',
            factor=0.2,
            patience=5,
            min_lr=1e-6
        )

        history = self.model.fit(
            train_dataset,
            validation_data=val_dataset,
            epochs=epochs,
            batch_size=batch_size,
            callbacks=[early_stopping, model_checkpoint, reduce_lr]
        )

        self.plot_training_history(history)
        return history

    def plot_training_history(self, history):
        """Plot training history"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

        # Accuracy
        ax1.plot(history.history['accuracy'], label='Train Accuracy')
        ax1.plot(history.history['val_accuracy'], label='Val Accuracy')
        ax1.set_title('Model Accuracy')
        ax1.set_xlabel('Epoch')
        ax1.set_ylabel('Accuracy')
        ax1.legend()

        # Loss
        ax2.plot(history.history['loss'], label='Train Loss')
        ax2.plot(history.history['val_loss'], label='Val Loss')
        ax2.set_title('Model Loss')
        ax2.set_xlabel('Epoch')
        ax2.set_ylabel('Loss')
        ax2.legend()

        plt.tight_layout()
        plt.savefig('cnn_training_history.png')
        plt.close()

    def evaluate(self, test_dataset):
        """Evaluasi model"""
        print("Evaluating CNN model...")
        results = self.model.evaluate(test_dataset)
        print(f"Test Loss: {results[0]:.4f}")
        print(f"Test Accuracy: {results[1]:.4f}")

        # Get predictions
        y_pred_probs = self.model.predict(test_dataset)
        y_pred = np.argmax(y_pred_probs, axis=1)

        return y_pred, results

    def save_model(self, path):
        """Simpan model"""
        self.model.save(path)
        print(f"Model saved to {path}")

    def load_model(self, path):
        """Load model"""
        self.model = keras.models.load_model(path)
        print(f"Model loaded from {path}")
```

## 4.5 Implementasi Model GCN

**File: `src/models/gcn_model.py`**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import GCNConv, global_mean_pool
from torch_geometric.data import Data, DataLoader
import numpy as np

class GCNModel(nn.Module):
    """Implementasi Graph Convolutional Network"""

    def __init__(self, num_node_features, hidden_dim=128, num_classes=None):
        super(GCNModel, self).__init__()
        self.conv1 = GCNConv(num_node_features, hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim // 2)
        self.fc1 = nn.Linear(hidden_dim // 2, 32)
        self.fc2 = nn.Linear(32, num_classes)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x, edge_index, batch):
        # Layer 1
        x = self.conv1(x, edge_index)
        x = F.relu(x)
        x = self.dropout(x)

        # Layer 2
        x = self.conv2(x, edge_index)
        x = F.relu(x)
        x = self.dropout(x)

        # Global pooling
        x = global_mean_pool(x, batch)

        # Fully connected layers
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)

        return F.log_softmax(x, dim=1)

class GCNTrainer:
    """Class untuk melatih GCN"""

    def __init__(self, model, device='cuda' if torch.cuda.is_available() else 'cpu'):
        self.model = model.to(device)
        self.device = device
        self.optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=5e-4)
        self.criterion = nn.NLLLoss()

    def train_epoch(self, train_loader):
        """Train satu epoch"""
        self.model.train()
        total_loss = 0

        for batch in train_loader:
            batch = batch.to(self.device)
            self.optimizer.zero_grad()

            out = self.model(batch.x, batch.edge_index, batch.batch)
            loss = self.criterion(out, batch.y)
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / len(train_loader)

    def evaluate(self, loader):
        """Evaluasi model"""
        self.model.eval()
        correct = 0
        total = 0

        with torch.no_grad():
            for batch in loader:
                batch = batch.to(self.device)
                out = self.model(batch.x, batch.edge_index, batch.batch)
                pred = out.argmax(dim=1)
                correct += (pred == batch.y).sum().item()
                total += batch.y.size(0)

        accuracy = correct / total
        return accuracy

    def train(self, train_loader, val_loader, epochs=200):
        """Train model"""
        best_val_acc = 0

        for epoch in range(epochs):
            train_loss = self.train_epoch(train_loader)
            val_acc = self.evaluate(val_loader)

            print(f'Epoch {epoch+1}/{epochs}, Loss: {train_loss:.4f}, Val Acc: {val_acc:.4f}')

            if val_acc > best_val_acc:
                best_val_acc = val_acc
                torch.save(self.model.state_dict(), 'best_gcn_model.pt')

        print(f'Best validation accuracy: {best_val_acc:.4f}')
        return best_val_acc

    def save_model(self, path):
        """Simpan model"""
        torch.save(self.model.state_dict(), path)
        print(f"Model saved to {path}")

    def load_model(self, path):
        """Load model"""
        self.model.load_state_dict(torch.load(path))
        print(f"Model loaded from {path}")
```

## 4.6 Implementasi Model Ensemble

**File: `src/models/ensemble_model.py`**

```python
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, StratifiedKFold
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
            n_jobs=-1
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
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix - Ensemble Model')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        plt.savefig('confusion_matrix_ensemble.png')
        plt.close()

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
```

## 4.7 Implementasi Model LLM

**File: `src/models/llm_model.py`**

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments
from datasets import Dataset
import json

class LLMFineTuner:
    """Class untuk fine-tuning LLM untuk keamanan siber"""

    def __init__(self, model_name='bert-base-uncased', max_length=512):
        self.model_name = model_name
        self.max_length = max_length
        self.tokenizer = None
        self.model = None

    def load_model(self):
        """Load pre-trained model dan tokenizer"""
        print(f"Loading model: {self.model_name}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

        # Add padding token if not exists
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        print("Model loaded successfully")

    def load_cyberllm_dataset(self, file_path):
        """Load dataset CyberLLMInstruct"""
        with open(file_path, 'r') as f:
            data = json.load(f)

        # Format untuk instruction tuning
        formatted_data = []
        for item in data:
            formatted_data.append({
                'instruction': item['instruction'],
                'input': item.get('input', ''),
                'output': item['output']
            })

        return formatted_data

    def tokenize_dataset(self, data):
        """Tokenize dataset"""
        def tokenize_function(examples):
            # Combine instruction and input
            text = examples['instruction'] + " " + examples['input']
            tokenized = self.tokenizer(
                text,
                truncation=True,
                padding='max_length',
                max_length=self.max_length,
                return_tensors='pt'
            )

            # Tokenize output as labels
            labels = self.tokenizer(
                examples['output'],
                truncation=True,
                padding='max_length',
                max_length=self.max_length,
                return_tensors='pt'
            )

            tokenized['labels'] = labels['input_ids']
            return tokenized

        dataset = Dataset.from_list(data)
        tokenized_dataset = dataset.map(tokenize_function, batched=True)
        return tokenized_dataset

    def fine_tune(self, train_dataset, val_dataset, output_dir='./fine_tuned_model'):
        """Fine-tune model"""
        print("Starting fine-tuning...")

        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=3,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            warmup_steps=500,
            weight_decay=0.01,
            logging_dir='./logs',
            logging_steps=100,
            evaluation_strategy='epoch',
            save_strategy='epoch',
            load_best_model_at_end=True,
            learning_rate=2e-5,
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=val_dataset,
            tokenizer=self.tokenizer,
        )

        trainer.train()
        trainer.save_model(output_dir)
        self.tokenizer.save_pretrained(output_dir)

        print(f"Fine-tuned model saved to {output_dir}")
        return trainer

    def generate_response(self, instruction, input_text='', max_length=256):
        """Generate response untuk instruction"""
        prompt = instruction + " " + input_text

        inputs = self.tokenizer(
            prompt,
            return_tensors='pt',
            truncation=True,
            max_length=self.max_length
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=max_length,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True
            )

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

    def save_model(self, path):
        """Simpan fine-tuned model"""
        self.model.save_pretrained(path)
        self.tokenizer.save_pretrained(path)
        print(f"Model saved to {path}")

    def load_fine_tuned_model(self, path):
        """Load fine-tuned model"""
        self.model = AutoModelForCausalLM.from_pretrained(path)
        self.tokenizer = AutoTokenizer.from_pretrained(path)
        print(f"Fine-tuned model loaded from {path}")
```

## 4.8 Implementasi Dashboard Web

### 4.8.1 Backend API

**File: `src/api/app.py`**

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load models
isolation_forest = joblib.load('data/models/isolation_forest.pkl')
ensemble_model = joblib.load('data/models/ensemble_rf.pkl')
# Load other models as needed

@app.route('/api/predict', methods=['POST'])
def predict():
    """Endpoint untuk prediksi"""
    data = request.json
    df = pd.DataFrame(data)

    # Preprocessing
    # ... (preprocessing steps)

    # Prediction
    prediction = ensemble_model.predict(df)
    probability = ensemble_model.predict_proba(df)

    return jsonify({
        'prediction': prediction.tolist(),
        'probability': probability.tolist()
    })

@app.route('/api/performance', methods=['GET'])
def get_performance():
    """Endpoint untuk mendapatkan metrik kinerja model"""
    performance = {
        'ensemble': {
            'accuracy': 0.96,
            'precision': 0.95,
            'recall': 0.94,
            'f1_score': 0.945
        },
        'isolation_forest': {
            'accuracy': 0.89,
            'precision': 0.87,
            'recall': 0.91,
            'f1_score': 0.89
        }
        # Add other models
    }
    return jsonify(performance)

@app.route('/api/threat-intel', methods=['POST'])
def threat_intelligence():
    """Endpoint untuk analisis intelijen ancaman menggunakan LLM"""
    data = request.json
    instruction = data.get('instruction', '')

    # Call LLM for analysis
    # response = llm_model.generate_response(instruction)

    response = "Threat analysis would be generated here"

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 4.8.2 Frontend Dashboard

**File: `dashboard/src/App.js`**

```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [performance, setPerformance] = useState(null);
  const [predictions, setPredictions] = useState(null);

  useEffect(() => {
    // Fetch model performance on load
    fetchPerformance();
  }, []);

  const fetchPerformance = async () => {
    try {
      const response = await axios.get('http://localhost:5000/api/performance');
      setPerformance(response.data);
    } catch (error) {
      console.error('Error fetching performance:', error);
    }
  };

  const handlePredict = async (data) => {
    try {
      const response = await axios.post('http://localhost:5000/api/predict', data);
      setPredictions(response.data);
    } catch (error) {
      console.error('Error predicting:', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cyber Security ML Dashboard</h1>
      </header>

      <div className="dashboard-content">
        {/* Performance Section */}
        <div className="section">
          <h2>Model Performance</h2>
          {performance && (
            <div className="performance-cards">
              {Object.entries(performance).map(([model, metrics]) => (
                <div key={model} className="card">
                  <h3>{model.toUpperCase()}</h3>
                  <p>Accuracy: {metrics.accuracy}</p>
                  <p>Precision: {metrics.precision}</p>
                  <p>Recall: {metrics.recall}</p>
                  <p>F1-Score: {metrics.f1_score}</p>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Prediction Section */}
        <div className="section">
          <h2>Threat Detection</h2>
          {/* Add form for input data */}
          <button onClick={() => handlePredict({})}>Predict</button>
          {predictions && (
            <div className="predictions">
              <h3>Prediction Results</h3>
              <p>Prediction: {predictions.prediction}</p>
              <p>Probability: {predictions.probability}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
```

## 4.9 Dokumentasi Kode Program

Seluruh kode program disertai dengan dokumentasi menggunakan docstring dan komentar yang jelas. Setiap modul memiliki README.md yang menjelaskan:

1. Tujuan modul
2. Dependensi yang diperlukan
3. Cara penggunaan
4. Contoh penggunaan

Selain itu, digunakan format docstring (Google Style atau NumPy Style) untuk setiap fungsi dan class untuk memudahkan dokumentasi otomatis dengan tools seperti Sphinx.

Kode program juga mengikuti PEP 8 style guide untuk Python dan ESLint untuk JavaScript untuk memastikan konsistensi dan readability.
