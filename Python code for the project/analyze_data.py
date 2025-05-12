# analyze_data.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("IFC_Dataset_Last10Years_CompleteInvested.csv")

# Rename column for convenience
investment_col = 'Total IFC investment as approved by Board(Million - USD)'

# Sectoral Analysis 
sector_stats = df.groupby('Industry')[investment_col].agg(
    count='count',
    mean='mean',
    median='median',
    min='min',
    max='max',
    std='std',
    q1=lambda x: x.quantile(0.25),
    q3=lambda x: x.quantile(0.75)
).sort_values(by='count', ascending=False)

# Save stats to a CSV
sector_stats.to_csv("Sector_Investment_Statistics.csv")
print("Sectoral investment stats saved to 'Sector_Investment_Statistics.csv'")

# Optional: Print a preview
print("Top 5 Sectors by Project Count:\n", sector_stats.head())

# --- Visualization ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Industry', y=investment_col)
plt.xticks(rotation=90)
plt.title("Total IFC Investment Distribution by Sector")
plt.tight_layout()
plt.savefig("Sector_Investment_Boxplot.png")
plt.show()
