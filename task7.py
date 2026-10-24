
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_inc5000.csv")

# Ensure numeric columns
for col in ["revenue", "growth", "workers", "yrs_on_list"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows missing key analysis values
df = df.dropna(subset=["company", "revenue", "growth", "industry"])

insights = []

# Insight 1: Highest revenue company
top_company = df.loc[df["revenue"].idxmax()]
insights.append(
    f"1. Highest Revenue Company: {top_company['company']} "
    f"with revenue {top_company['revenue']:,.0f}."
)

# Insight 2: Lowest revenue company
low_company = df.loc[df["revenue"].idxmin()]
insights.append(
    f"2. Lowest Revenue Company: {low_company['company']} "
    f"with revenue {low_company['revenue']:,.0f}."
)

# Insight 3: Industry with the most companies
industry_counts = df["industry"].value_counts()
insights.append(
    f"3. Most Represented Industry: {industry_counts.index[0]} "
    f"with {industry_counts.iloc[0]} companies."
)

# Insight 4: Highest average revenue by industry
industry_summary = df.groupby("industry").agg(
    company_count=("company", "count"),
    average_revenue=("revenue", "mean"),
    average_growth=("growth", "mean")
)

best_revenue_industry = industry_summary["average_revenue"].idxmax()
best_revenue_data = industry_summary.loc[best_revenue_industry]

insights.append(
    f"4. Highest Average Revenue Industry: {best_revenue_industry}; "
    f"average revenue {best_revenue_data['average_revenue']:,.2f}, "
    f"based on {int(best_revenue_data['company_count'])} companies."
)

# Insight 5: Highest average growth by industry
best_growth_industry = industry_summary["average_growth"].idxmax()
best_growth_data = industry_summary.loc[best_growth_industry]

insights.append(
    f"5. Highest Average Growth Industry: {best_growth_industry}; "
    f"average growth {best_growth_data['average_growth']:.2f}."
)

# Recommendations
recommendations = [
    "1. Study the business practices of high-revenue companies "
    "to identify approaches that may be useful for other businesses.",

    "2. Compare revenue and growth across industries before deciding "
    "where to invest resources. Consider company counts and market risks.",

    "3. Investigate lower-revenue companies to understand possible "
    "challenges; revenue alone does not prove poor performance."
]

# Display report
report = []
report.append("TASK 7: BUSINESS INSIGHTS & RECOMMENDATIONS")
report.append("=" * 50)

report.append("\nBUSINESS INSIGHTS")
report.extend(insights)

report.append("\nBUSINESS RECOMMENDATIONS")
report.extend(recommendations)

report.append(
    "\nNote: Findings describe the Inc5000 Company List 2014 dataset. "
    "They do not represent a Sales dashboard analysis."
)

full_report = "\n".join(report)
print(full_report)

# Save report to a text file
with open("task7_business_insights.txt", "w", encoding="utf-8") as file:
    file.write(full_report)

print("\nReport saved as task7_business_insights.txt")
