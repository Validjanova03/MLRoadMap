import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
column_names = [
    "sepal_length", "sepal_width", "petal_length", "petal_width", "species"
]
df = pd.read_csv("iris.data",names=column_names)
print(df.head())
print(df.shape)

X =df.drop("species", axis=1)
y=df["species"]

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print("Accuracy:", accuracy)


predictions = model.predict(X_test)
print("Predictions:", predictions[:10])

print("\nActual: " ,y_test[:10].values)
acc = accuracy_score(y_test,predictions)
print("\n Accuracy Score:",acc)

models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(random_state=42)
}
print("\nModel Comparison:")
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"{name}: Accuracy = {acc:.2f}")
