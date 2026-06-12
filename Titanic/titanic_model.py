import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

df= pd.read_csv('train.csv')
print(df.shape)
df = df.drop("Cabin", axis=1)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Sex"] = df["Sex"].map({
    "male":0,
    "female":1
})
features =[
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]
X = df[features]
y = df["Survived"]  
X_train, X_test, y_train,y_test = train_test_split(X,y, test_size = 0.2,random_state = 42)
model = LogisticRegression(max_iter = 1000)
model.fit(X_train,y_train)
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:",accuracy)
print("\nFirst 10 Predictions:")
print(predictions[:10])
print("\nActual values:")
print(y_test.iloc[:10].values)
cm = confusion_matrix(y_test, predictions)

plt.figure(figsize=(5,4))
plt.imshow(cm)

plt.title("Confusion Matrix")
plt.colorbar()

plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.xticks([0,1], ["Died","Survived"])
plt.yticks([0,1], ["Died","Survived"])

for i in range(2):
    for j in range(2):
        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )

plt.tight_layout()
plt.show()
print(classification_report(y_test, predictions))

