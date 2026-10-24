
import pandas as pd

df = pd.read_csv("data/cleaned_inc5000.csv")

print("BUSINESS INSIGHTS AND RECOMMENDATIONS")
print("=" * 45)

# Insight 1: Top company by revenue
top_company = df.loc[df["revenue"].idxmax()]
print("\n1. Highest Revenue Company")
print("Company:", top_company["company"])
print("Revenue:", top_company["revenue"])
print("Recommendation: Study this company's industry and business model.")

# Insight 2: Top company by growth
top_growth = df.loc[df["growth"].idxmax()]
print("\n2. Highest Growth Company")
print("Company:", top_growth["company"])
print("Growth:", top_growth["growth"])
print("Recommendation: Explore the factors contributing to its growth.")

# Insight 3: Most common industry
industry_counts = df["industry"].value_counts()
print("\n3. Industry with Most Companies")
print("Industry:", industry_counts.index[0])
print("Company count:", industry_counts.iloc[0])
print("Recommendation: Compare competition and opportunities in this industry.")

# Insight 4: Industry with highest average revenue
avg_revenue = df.groupby("industry")["revenue"].mean()
best_industry = avg_revenue.idxmax()
print("\n4. Highest Average Revenue Industry")
print("Industry:", best_industry)
print("Average revenue:", round(avg_revenue.max(), 2))
print("Recommendation: Investigate what drives revenue in this industry.")

# Insight 5: Average growth
average_growth = df["growth"].mean()
print("\n5. Overall Average Growth")
print("Average growth:", round(average_growth, 2))
print("Recommendation: Compare company growth with the dataset average.")

print("\nAnalysis completed!")
