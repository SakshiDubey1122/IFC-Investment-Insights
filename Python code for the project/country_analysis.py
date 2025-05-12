# country_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("IFC_Dataset_Last10Years_CompleteInvested.csv")

# Rename investment column for convenience
investment_col = 'Total IFC investment as approved by Board(Million - USD)'

# --- Country-Level Analysis ---
country_stats = df.groupby('Country')[investment_col].agg(
    project_count='count',
    total_investment='sum',
    avg_investment='mean',
    median_investment='median',
    max_investment='max',
    min_investment='min'
).sort_values(by='total_investment', ascending=False)

# Save stats to a CSV
country_stats.to_csv("Country_Investment_Statistics.csv")
print("Country-level investment stats saved to 'Country_Investment_Statistics.csv'")

# Optional: Print a preview
print("\nTop 5 Countries by Total Investment:\n", country_stats.head())

# --- Visualization ---
plt.figure(figsize=(12, 6))
top_countries = country_stats.head(10).reset_index()
sns.barplot(data=top_countries, x='Country', y='total_investment', palette="viridis")
plt.title("Top 10 Countries by Total IFC Investment (Last 10 Years)")
plt.ylabel("Total Investment (Million USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Top10_Country_Investment_Barplot.png")
plt.show()
