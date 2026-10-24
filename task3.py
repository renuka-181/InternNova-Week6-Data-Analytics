import pandas as pd
import os

# Load dataset
file_path = "data/Data Set- Inc5000 Company List_2014.csv"
df = pd.read_csv(file_path)

print("Original dataset shape:", df.shape)

# Remove columns that are completely empty
empty_columns = df.columns[df.isnull().all()].tolist()
df = df.dropna(axis=1, how="all")

print("Removed completely empty columns:", empty_columns)

# Fill missing metro values
if "metro" in df.columns:
    df["metro"] = df["metro"].fillna("Unknown")

# Check missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Save cleaned dataset
os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_inc5000.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("Final dataset shape:", df.shape)