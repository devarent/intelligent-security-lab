"""
Feature Engineering Module
Handles normalization, encoding, and feature creation
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder

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
