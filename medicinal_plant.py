import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("pfaf_plants_merged.csv")

# Ensure numeric types for ratings
df['Edibility Rating'] = pd.to_numeric(df['edibility_rating_search'], errors='coerce')
df['Medicinal Rating'] = pd.to_numeric(df['medicinal_rating_search'], errors='coerce')

# Drop rows with missing ratings
df = df.dropna(subset=['Edibility Rating', 'Medicinal Rating', 'Weed Potential'])

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Edibility Rating',
    y='Medicinal Rating',
    hue='Weed Potential',
    data=df,
    palette='Set1',
    s=100,
    alpha=0.7
)
plt.title('Edibility vs Medicinal Rating by Weed Potential')
plt.xlabel('Edibility Rating')
plt.ylabel('Medicinal Rating')
plt.legend(title='Weed Potential')
plt.grid(True)
plt.tight_layout()
plt.show()
