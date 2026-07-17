import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("train.csv")
df = df.drop(columns = ["Name", "Ticket", "Cabin", "PassengerId"])
# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Encode categorical variables
df["Sex"] = LabelEncoder().fit_transform(df["Sex"])
df["Embarked"] = LabelEncoder().fit_transform(df["Embarked"])

X = df.drop(columns=["Survived"])
y = df["Survived"]

FEATURE_NAMES = X.columns.tolist()

# Train/Test split
X_train,X_test , y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42,stratify= y)
print("=" *55)
print("TITANIC - Decision Tree vs Random Forest")
print("=" *55)
print(f"\nTrain rows: {len(X_train)}")
print(f"Test rows: {len(X_test)}")
print(f"Features: {len(FEATURE_NAMES)}")

# Train both models
tree = DecisionTreeClassifier(random_state=42, max_depth=5)
forest = RandomForestClassifier(random_state=42, n_estimators=500, n_jobs=-1)

tree.fit(X_train, y_train)
forest.fit(X_train, y_train)


# Accuracy - Train vs Test
tree_train = tree.score(X_train,y_train)
tree_test = tree.score(X_test,y_test)
forest_train = forest.score(X_train,y_train)
forest_test = forest.score(X_test,y_test)
print("─" * 55)
print(f"{'Model':<22} {'Train Acc':>10} {'Test Acc':>10} {'Gap':>8}")
print("─" * 55)
print(f"{'Decision Tree':<22} {tree_train:>10.3f} {tree_test:>10.3f} {tree_train - tree_test:>8.3f}")
print(f"{'Random Forest':<22} {forest_train:>10.3f} {forest_test:>10.3f} {forest_train - forest_test:>8.3f}")
print("─" * 55)
print("Gap = train − test. Smaller gap = less overfitting.\n")



# Cross Validation
tree_cv   = cross_val_score(tree,   X, y, cv=5)
forest_cv = cross_val_score(forest, X, y, cv=5)
 
print("─" * 55)
print(f"{'Model':<22} {'CV Mean':>10} {'CV Std':>10}")
print("─" * 55)
print(f"{'Decision Tree':<22} {tree_cv.mean():>10.3f} {tree_cv.std():>10.3f}")
print(f"{'Random Forest':<22} {forest_cv.mean():>10.3f} {forest_cv.std():>10.3f}")
print("─" * 55)
print("Std = stability. Lower std = more consistent.\n")


# Classification Report
print("── Decision Tree ──────────────────────────────────")
print(classification_report(y_test, tree.predict(X_test),
      target_names=["Not Survived", "Survived"]))
 
print("── Random Forest ──────────────────────────────────")
print(classification_report(y_test, forest.predict(X_test),
      target_names=["Not Survived", "Survived"]))


# Feature Importance - Forest 
print("── Feature Importance (Random Forest) ─────────────")
importances = pd.Series(forest.feature_importances_, index=FEATURE_NAMES)
importances = importances.sort_values(ascending=False)
for feat, imp in importances.items():
    bar = "=" * int(imp * 50)
    print(f"  {feat:<12} {bar:<25} {imp:.3f}")
print()

# Plots
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Decision Tree vs Random Forest — Titanic", fontsize=13, fontweight="bold")
 
 
# ── Plot 1: Train vs Test Accuracy Bar Chart ──
models      = ["Decision\nTree", "Random\nForest"]
train_accs  = [tree_train, forest_train]
test_accs   = [tree_test,  forest_test]
x           = np.arange(len(models))
width       = 0.35
 
axes[0].bar(x - width/2, train_accs, width, label="Train", color="#4f8ef7", alpha=0.85)
axes[0].bar(x + width/2, test_accs,  width, label="Test",  color="#22c55e", alpha=0.85)
axes[0].set_ylim(0.5, 1.05)
axes[0].set_xticks(x)
axes[0].set_xticklabels(models)
axes[0].set_ylabel("Accuracy")
axes[0].set_title("Train vs Test Accuracy")
axes[0].legend()
axes[0].axhline(0.8, color="gray", linestyle="--", linewidth=0.8, alpha=0.6)
for i, (tr, te) in enumerate(zip(train_accs, test_accs)):
    axes[0].text(i - width/2, tr + 0.005, f"{tr:.2f}", ha="center", fontsize=9)
    axes[0].text(i + width/2, te + 0.005, f"{te:.2f}", ha="center", fontsize=9)
 
 
# ── Plot 2: Feature Importance ──
importances.sort_values().plot(
    kind="barh", ax=axes[1], color="#4f8ef7", alpha=0.85
)
axes[1].set_title("Feature Importance (Random Forest)")
axes[1].set_xlabel("Importance score")
  
plt.tight_layout()
plt.savefig("tree_vs_forest.png", dpi=150, bbox_inches="tight")
print("Plot saved → tree_vs_forest.png")
plt.show()
