# netflix_analysis.py
# Minimal script — run locally or on Google Colab after uploading netflix_titles.csv

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')  # upload file to repo or to Colab session
counts = df['release_year'].value_counts().sort_index().tail(10)
counts.plot(kind='bar')
plt.title('Top 10 Years with Most Releases')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('netflix-analysis/top_release_years.png')
print("Saved plot to netflix-analysis/top_release_years.png")
