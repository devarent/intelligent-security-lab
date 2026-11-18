"""
Imbalance Handler Module
Handles class imbalance using SMOTE and other techniques
"""

import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE
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
