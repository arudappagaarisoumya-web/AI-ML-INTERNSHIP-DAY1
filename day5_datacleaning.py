import pandas as pd
# Load the dataset
df = pd.read_csv("student_scores.csv")
print("Original Dataset:")
print(df)

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Fill missing numerical values with the mean
df["Maths"] = df["Maths"].fillna(df["Maths"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())

# 2. Check and remove duplicates
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()

# 3. Display statistical information
print("\nStatistical Summary:")
print(df.describe())

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Save cleaned dataset
df.to_csv("cleaned_student_scores.csv", index=False)
print("\nCleaned dataset saved successfully!")