
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("data/cleaned_inc5000.csv")

os.makedirs("charts", exist_ok=True)
sns.set_theme()

# Chart 1: Top 10 companies by revenue
top_revenue = df.nlargest(10, "revenue").sort_values("revenue")

plt.figure(figsize=(10, 6))
plt.barh(top_revenue["company"], top_revenue["revenue"])
plt.title("Top 10 Companies by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("charts/chart1_top_revenue.png")
plt.show()
plt.close()

# Chart 2: Top 10 industries by number of companies
industry_counts = df["industry"].value_counts().head(10).sort_values()

plt.figure(figsize=(10, 6))
industry_counts.plot(kind="barh")
plt.title("Top 10 Industries by Company Count")
plt.xlabel("Number of Companies")
plt.tight_layout()
plt.savefig("charts/chart2_industries.png")
plt.show()
plt.close()

# Chart 3: Revenue distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["revenue"], bins=30)
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.tight_layout()
plt.savefig("charts/chart3_revenue_distribution.png")
plt.show()
plt.close()

# Chart 4: Growth distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["growth"], bins=30)
plt.title("Growth Distribution")
plt.xlabel("Growth")
plt.tight_layout()
plt.savefig("charts/chart4_growth_distribution.png")
plt.show()
plt.close()

# Chart 5: Average revenue by top 10 industries
avg_revenue = (
    df.groupby("industry")["revenue"]
    .mean()
    .nlargest(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
avg_revenue.plot(kind="barh")
plt.title("Top 10 Industries by Average Revenue")
plt.xlabel("Average Revenue")
plt.tight_layout()
plt.savefig("charts/chart5_avg_revenue.png")
plt.show()
plt.close()

print("All 5 charts saved in the charts folder!")
