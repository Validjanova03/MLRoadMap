# Random Forest

> A Random Forest is a group of Decision Trees voting together. The majority wins.

---

## Why not just use one Decision Tree?

A single tree is **unstable** — show it slightly different data and it builds a completely different tree. This is called **high variance**.

---

## The fix

Train **500 different trees**, each on a random slice of data. Every tree votes. **Majority vote = final prediction.**

```
Tree 1  → Yes
Tree 2  → Yes
Tree 3  → No
Tree 4  → Yes
Tree 5  → No
           ↓
     3 Yes, 2 No → Predict: YES
```

---

## The analogy

> Ask **one friend** if a stock will rise — risky.
> Ask **500 people** who each read different reports — take the majority vote.
> The crowd is almost always smarter than any individual.

---

## How each tree is made different — Bagging

**Bagging = Bootstrap sampling + Aggregating**

| Step | What happens |
|------|-------------|
| **Random rows** | Each tree trains on a random sample of rows (with replacement) |
| **Random features** | At each split, only √n features are tried — not all |

Because each tree sees different data → makes different mistakes → averaging 500 different mistakes cancels them out → what's left is the signal.

---

## Single Tree vs Random Forest

| | Single Tree | Random Forest |
|--|-------------|---------------|
| Training data | Sees all rows | Each tree sees random rows |
| Features per split | All features | Random √n features |
| Speed | Fast | Slower |
| Accuracy | Lower | Higher |
| Overfitting | Overfits easily | Rarely overfits |
| Explainability | Easy to read | Black box |
| Use when | Need to explain decisions | Need best accuracy |

---

## Feature Importance

After training, Random Forest tells you **which features mattered most** across all trees.

```python
rf.feature_importances_
# → [0.28, 0.22, 0.20, 0.16, 0.05, ...]
# Values always sum to 1.0
```

Features used in early splits (close to root) across many trees → higher importance.
Use this to drop useless features from your model.

### Example — Titanic dataset

| Feature | Importance |
|---------|------------|
| Sex | 0.28 |
| Fare | 0.22 |
| Age | 0.20 |
| Pclass | 0.16 |
| SibSp | 0.05 |
| Parch | 0.04 |
| Embarked | 0.03 |
| Cabin | 0.02 |

> Sex, Fare, and Age alone explain 70% of survival.

---

## sklearn code

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

rf = RandomForestClassifier(
    n_estimators=500,     # number of trees — more = more stable
    max_features="sqrt",  # random features per split
    n_jobs=-1,            # use all CPU cores
    random_state=42
)

rf.fit(X_train, y_train)

print(f"Train: {rf.score(X_train, y_train):.2f}")
print(f"Test:  {rf.score(X_test, y_test):.2f}")
print(f"Feature importances: {rf.feature_importances_}")
```

### Compare single tree vs forest

```python
from sklearn.tree import DecisionTreeClassifier

tree   = DecisionTreeClassifier(random_state=42)
forest = RandomForestClassifier(n_estimators=500, random_state=42, n_jobs=-1)

tree_scores   = cross_val_score(tree,   X, y, cv=5)
forest_scores = cross_val_score(forest, X, y, cv=5)

print(f"Single tree:   {tree_scores.mean():.3f} ± {tree_scores.std():.3f}")
print(f"Random forest: {forest_scores.mean():.3f} ± {forest_scores.std():.3f}")
# The ± number shows variance — forest will always be lower
```

### Feature importance plot

```python
import matplotlib.pyplot as plt
import pandas as pd

feat_imp = pd.Series(rf.feature_importances_, index=feature_names)
feat_imp.sort_values().plot(kind="barh", figsize=(8, 5))
plt.title("Feature Importance")
plt.xlabel("Importance score")
plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150)
```

---

## Key parameters

| Parameter | Default | What it does |
|-----------|---------|-------------|
| `n_estimators` | 100 | Number of trees — more = more stable, slower |
| `max_features` | `"sqrt"` | Features tried at each split |
| `max_depth` | None | Depth limit per tree (usually not needed) |
| `min_samples_leaf` | 1 | Min samples in a leaf — tune to reduce overfitting |
| `n_jobs` | 1 | Set to `-1` to use all CPU cores |
| `random_state` | None | Always set for reproducibility |

---

## The one thing to remember

> A Decision Tree is one person's opinion.
> A Random Forest is 500 people who each looked at different information, voting together.
> The majority is almost always right.
