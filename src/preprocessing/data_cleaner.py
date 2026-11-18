"""
Data Cleaning Module
Handles missing values, duplicates, and outliers
"""

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
