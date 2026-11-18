"""
Data Splitter Module
Handles train/validation/test splitting
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold

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
