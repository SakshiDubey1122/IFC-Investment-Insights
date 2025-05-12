import pandas as pd

df = pd.read_csv("IFC_Dataset_Last10Years_CompleteInvested.csv")

# Selecting only relevant columns
columns_to_keep = [
    'Date Disclosed', 'Country', 'Industry', 'Status',
    'IFC investment for Loan(Million - USD)',
    'IFC investment for Equity(Million - USD)',
    'Total IFC investment as approved by Board(Million - USD)'
]
df_reduced = df[columns_to_keep]

# Save reduced version
df_reduced.to_csv("IFC_Dataset_PowerBI.csv", index=False)
