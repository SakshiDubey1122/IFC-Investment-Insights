import pandas as pd
from datetime import datetime

# Load the dataset
df = pd.read_csv("IFC_Dataset.csv")

# Drop columns with over 90% missing values
columns_to_drop = [
    'IFC investment for Risk Management(Million - USD)',
    'IFC investment for Guarantee(Million - USD)'
]
df_cleaned = df.drop(columns=columns_to_drop)

# Fill missing text fields with "Unknown"
text_columns = ['Company Name', 'Product Line', 'IFC Country Code', 'WB Country Code']
for col in text_columns:
    df_cleaned[col] = df_cleaned[col].fillna("Unknown")

# Fill numeric investment columns with 0
numeric_columns_to_fill = [
    'IFC investment for Loan(Million - USD)',
    'IFC investment for Equity(Million - USD)',
    'Total IFC investment as approved by Board(Million - USD)'
]
df_cleaned[numeric_columns_to_fill] = df_cleaned[numeric_columns_to_fill].fillna(0)

# Convert date columns to datetime format
df_cleaned['Date Disclosed'] = pd.to_datetime(df_cleaned['Date Disclosed'], errors='coerce')
df_cleaned['IFC Invested Date'] = pd.to_datetime(df_cleaned['IFC Invested Date'], errors='coerce')

# Drop rows where 'Date Disclosed' is missing
df_cleaned = df_cleaned.dropna(subset=['Date Disclosed'])

# Filter data from the last 10 years
cutoff_date = pd.Timestamp(datetime.now().year - 10, 1, 1)
df_last_10_years = df_cleaned[df_cleaned['Date Disclosed'] >= cutoff_date]

# Remove rows where 'IFC Invested Date' is missing
df_last_10_years = df_last_10_years.dropna(subset=['IFC Invested Date'])

# Sort by 'Date Disclosed'
df_last_10_years = df_last_10_years.sort_values(by='Date Disclosed')

# Save the final result
df_last_10_years.to_csv("IFC_Dataset_Last10Years_CompleteInvested.csv", index=False)

print("Cleaned, filtered, and sorted dataset saved as 'IFC_Dataset_Last10Years_CompleteInvested.csv'")

