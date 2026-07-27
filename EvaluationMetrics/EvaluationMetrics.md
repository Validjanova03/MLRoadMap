# 📊 Evaluation Metrics for Classification (NumPy Only)

When building a machine learning classification model, training the model is only half of the work. We also need to **measure how well the model performs**. This is where **evaluation metrics** come in.

Different metrics provide different insights about a model's performance. Some metrics focus on overall correctness, while others are more useful when dealing with **imbalanced datasets**.

---

# 1️⃣ Confusion Matrix

The **Confusion Matrix** is the foundation of almost every classification metric.

It compares the **actual labels** with the **predicted labels** and tells us exactly where the model made correct and incorrect predictions.

For binary classification, there are four possible outcomes:
| Actual | Predicted | Meaning |
|---------|-----------|---------|
| Positive | Positive | ✅ True Positive (TP) |
| Positive | Negative | ❌ False Negative (FN) |
| Negative | Positive | ❌ False Positive (FP) |
| Negative | Negative | ✅ True Negative (TN) |

### Example

```
                Predicted
              Positive  Negative

Actual Positive    TP        FN
Actual Negative    FP        TN
```

The confusion matrix helps us understand **what type of mistakes the model makes**, not just how many.

---

# 2️⃣ Accuracy
Accuracy measures the percentage of predictions that are correct.

### Formula

\[
Accuracy = \frac{TP + TN}{TP + TN + FP + FN}
\]

### Simple Explanation

If your model makes **100 predictions** and **92 are correct**, then the accuracy is:

```
Accuracy = 92%
```

### When to Use

✅ Balanced datasets

### When Not to Use

If one class appears much more often than another, accuracy can be misleading.

Example:

```
99 Cats
1 Dog
```

If the model predicts **Cat every time**, accuracy is:

```
99%
```

But the model never detects dogs.

---

# 3️⃣ Precision
