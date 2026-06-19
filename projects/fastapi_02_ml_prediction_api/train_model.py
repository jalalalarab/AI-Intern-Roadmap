from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Load the classic Iris dataset (150 flower samples, 4 measurements each, 3 species)
iris = load_iris()
X, y = iris.data, iris.target

# Split into training data and test data, so we can check accuracy honestly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple Logistic Regression classifier
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Check accuracy on data it hasn't seen
accuracy = model.score(X_test, y_test)
print(f"Model accuracy: {accuracy:.2f}")

# Save the trained model to a file
joblib.dump(model, "iris_model.joblib")
print("Model saved as iris_model.joblib")