
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_inc5000.csv")

print("DATASET OVERVIEW")
print("Total companies:", len(df))
print("Total columns:", len(df.columns))

# 1. Top 10 companies by revenue
print("\n1. TOP 10 COMPANIES BY REVENUE")
print(
    df.nlargest(10, "revenue")[["company", "revenue", "industry"]]
    .to_string(index=False)
)

# 2. Top 10 companies by growth
print("\n2. TOP 10 COMPANIES BY GROWTH")
print(
    df.nlargest(10, "growth")[["company", "growth", "industry"]]
    .to_string(index=False)
)

# 3. Top 10 industries by company count
print("\n3. TOP 10 INDUSTRIES BY COMPANY COUNT")
print(df["industry"].value_counts().head(10).to_string())

# 4. Average revenue by industry
print("\n4. TOP INDUSTRIES BY AVERAGE REVENUE")
print(
    df.groupby("industry")["revenue"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .round(2)
    .to_string()
)

# 5. Summary statistics
print("\n5. SUMMARY STATISTICS")
print(
    df[["workers", "growth", "revenue", "yrs_on_list"]]
    .describe()
    .round(2)
)

# Save industry summary
summary = df.groupby("industry").agg(
    company_count=("company", "count"),
    average_revenue=("revenue", "mean"),
    average_growth=("growth", "mean")
).round(2)

summary.to_csv("data/industry_summary.csv")

print("\nAnalysis completed successfully!")
print("Saved: data/industry_summary.csv")
