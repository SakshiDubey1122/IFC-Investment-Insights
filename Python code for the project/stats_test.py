# stat_tests.py

import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("IFC_Dataset_Last10Years_CompleteInvested.csv")

# Select numeric columns for correlation analysis
numeric_cols = [
    'IFC investment for Loan(Million - USD)',
    'IFC investment for Equity(Million - USD)',
    'Total IFC investment as approved by Board(Million - USD)'
]

df_numeric = df[numeric_cols]

# Pearson Correlation (linear)
pearson_corr = df_numeric.corr(method='pearson')
pearson_corr.to_csv("Pearson_Correlation_Matrix.csv")
print("Pearson correlation matrix saved to 'Pearson_Correlation_Matrix.csv'")

# Spearman Correlation (monotonic/rank)
spearman_corr = df_numeric.corr(method='spearman')
spearman_corr.to_csv("Spearman_Correlation_Matrix.csv")
print("Spearman correlation matrix saved to 'Spearman_Correlation_Matrix.csv'")

# Optional preview
print("\nPearson Correlation:\n", pearson_corr)
print("\nSpearman Correlation:\n", spearman_corr)
