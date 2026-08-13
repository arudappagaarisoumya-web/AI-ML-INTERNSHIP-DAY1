import pandas as pd

# Load the student score dataset
data = pd.read_csv("student_scores.csv")

# Display the complete dataset
print("Student Score Dataset:")
print(data)

# Display first 5 rows
print("\nFirst 5 Rows:")
print(data.head())

# Display number of rows and columns
print("\nNumber of Rows and Columns:")
print(data.shape)

# Display column names
print("\nColumn Names:")
print(data.columns)

# Display dataset information
print("\nDataset Information:")
print(data.info())