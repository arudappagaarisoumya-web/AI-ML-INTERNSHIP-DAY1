from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data: Study hours and marks
X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [35, 40, 50, 55, 60, 65, 75, 80]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train)
print("Testing data:", X_test)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict marks for 9 hours of study
prediction = model.predict([[9]])

print("Predicted marks for 9 hours:", prediction[0])