"""
Isolation Forest Model for Anomaly Detection
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
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
        try:
            plt.figure(figsize=(8, 6))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
            plt.title('Confusion Matrix - Isolation Forest')
            plt.ylabel('True Label')
            plt.xlabel('Predicted Label')
            plt.savefig('confusion_matrix_isolation_forest.png')
            plt.close()
        except:
            pass

        return y_pred_binary

    def save_model(self, path):
        """Simpan model ke disk"""
        joblib.dump(self.model, path)
        print(f"Model saved to {path}")

    def load_model(self, path):
        """Load model dari disk"""
        self.model = joblib.load(path)
        print(f"Model loaded from {path}")
