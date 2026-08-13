from sklearn.linear_model import LinearRegression

# Dataset
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [35, 40, 50, 55, 60, 65, 75, 80]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

print("Model trained successfully!")

# Make a prediction
prediction = model.predict([[9]])

print("Predicted marks for 9 hours of study:", prediction[0])