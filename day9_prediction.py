from sklearn.linear_model import LinearRegression

# Student dataset
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [35, 40, 50, 55, 60, 65, 75, 80]

# Create and train the model
model = LinearRegression()
model.fit(X, y)

print("Model trained successfully!")

# Predict scores for different study hours
study_hours = [[2], [5], [7], [9]]

predictions = model.predict(study_hours)

# Display predictions
for hours, score in zip(study_hours, predictions):
    print(f"Study Hours: {hours[0]} -> Predicted Score: {score:.2f}")