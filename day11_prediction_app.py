from sklearn.linear_model import LinearRegression

# Student dataset
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [35, 40, 50, 55, 60, 65, 75, 80]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

print("Student Score Prediction App")
print("-----------------------------")

# Get study hours from user
hours = float(input("Enter your study hours: "))

# Predict score
prediction = model.predict([[hours]])

print(f"Predicted score: {prediction[0]:.2f}")