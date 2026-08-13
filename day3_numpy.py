import numpy as np
# Creating a NumPy array
numbers = np.array([10, 20, 30, 40, 50])

print("Original Array:")
print(numbers)

# Indexing
print("\nFirst element:", numbers[0])
print("Third element:", numbers[2])

# Mathematical operations
print("\nAddition:")
print(numbers + 5)

print("\nSubtraction:")
print(numbers - 5)

print("\nMultiplication:")
print(numbers * 2)

print("\nDivision:")
print(numbers / 2)

# Array calculations
print("\nSum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))