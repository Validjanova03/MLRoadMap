import pandas as pd

from sklearn.linear_model import LogisticRegression
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

# Handle Missing Values

train_df["Age"] = train_df["Age"].fillna(
    train_df["Age"].median()
)

test_df["Age"] = test_df["Age"].fillna(
    test_df["Age"].median()
)

train_df["Embarked"] = train_df["Embarked"].fillna(
    train_df["Embarked"].mode()[0]
)

test_df["Fare"] = test_df["Fare"].fillna(
    test_df["Fare"].median()
)

# Convert Categorical Data
train_df["Sex"] = train_df["Sex"].map({
    "male": 0,
    "female": 1
})

test_df["Sex"] = test_df["Sex"].map({
    "male": 0,
    "female": 1
})

# Select Features
features = [
    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare"
]

X_train = train_df[features]
y_train = train_df["Survived"]

X_test = test_df[features]

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train, y_train)

# Predict 

predictions = model.predict(X_test)

# Create Submission File
submission = pd.DataFrame({
    "PassengerId": test_df["PassengerId"],
    "Survived": predictions
})

submission.to_csv(
    "submission.csv",
    index=False
)

print("submission.csv created successfully!")
print(submission.head())
