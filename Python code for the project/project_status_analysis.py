# status_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("IFC_Dataset_Last10Years_CompleteInvested.csv")

# Rename investment column for convenience
investment_col = 'Total IFC investment as approved by Board(Million - USD)'

# Project Status Analysis 
status_stats = df.groupby('Status')[investment_col].agg(
    project_count='count',
    total_investment='sum',
    avg_investment='mean',
    median_investment='median'
).sort_values(by='total_investment', ascending=False)

# Save stats to CSV
status_stats.to_csv("Status_Investment_Statistics.csv")
print("Project Status-level investment stats saved to 'Status_Investment_Statistics.csv'")

# Optional: Print a preview
print("Project Status Summary:\n", status_stats)

# Visualization 
plt.figure(figsize=(8, 6))
sns.barplot(x=status_stats.index, y=status_stats['total_investment'], hue=status_stats.index, palette="pastel", legend=False)

plt.title("Total IFC Investment by Project Status")
plt.ylabel("Total Investment (Million USD)")
plt.xlabel("Project Status")
plt.tight_layout()
plt.savefig("Project_Status_Investment_Barplot.png")
plt.show()
