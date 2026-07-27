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

Precision tells us:

> **When the model predicts Positive, how often is it correct?**

### Formula

\[
Precision = \frac{TP}{TP + FP}
\]

### Example

Suppose a model predicts:

- 20 emails are spam
- Only 15 are actually spam

Then

```
Precision = 15 / 20 = 75%
```

### High Precision Means

- Few false positives
- Predictions are trustworthy

### Useful For

- Spam detection
- Fraud detection
- Medical diagnosis

where false alarms are expensive.

---

# 4️⃣ Recall (Sensitivity)

Recall answers a different question:

> **Out of all actual positive samples, how many did the model find?**

### Formula

\[
Recall = \frac{TP}{TP + FN}
\]

### Example

There are 100 patients with a disease.

The model correctly identifies 90 of them.

```
Recall = 90 / 100 = 90%
```

### High Recall Means

- Very few false negatives
- The model rarely misses positive cases

Useful when **missing a positive case is dangerous**.

Examples:

- Cancer detection
- Fraud detection
- Security systems

---

# 5️⃣ Specificity

Specificity measures how well the model identifies **negative samples**.

### Formula

\[
Specificity = \frac{TN}{TN + FP}
\]

### Simple Explanation

If there are 200 healthy patients and the model correctly identifies 190 of them:

```
Specificity = 190 / 200 = 95%
```

### High Specificity Means

- Few false positives
- Negative predictions are reliable

---

# 6️⃣ F1 Score

Sometimes we want to balance **Precision** and **Recall**.

The **F1 Score** combines both into a single number.

### Formula

\[
F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall}
\]

### Why Not Use the Average?

Instead of the arithmetic mean, the F1 Score uses the **harmonic mean**, which penalizes models that perform poorly on either precision or recall.

### Example

```
Precision = 0.90
Recall = 0.60

F1 ≈ 0.72
```

Even though precision is high, the lower recall reduces the final score.

---

# 7️⃣ False Positive Rate (FPR)

False Positive Rate measures:

> **How often negative samples are incorrectly classified as positive.**

### Formula

\[
FPR = \frac{FP}{FP + TN}
\]

### Example

Among 100 healthy patients:

- 10 are incorrectly diagnosed as sick.

```
FPR = 10%
```

Lower is better.

---

# 8️⃣ False Negative Rate (FNR)

False Negative Rate measures:

> **How often positive samples are missed.**

### Formula

\[
FNR = \frac{FN}{FN + TP}
\]

### Example

Out of 50 patients with cancer,

5 are incorrectly classified as healthy.

```
FNR = 10%
```

Lower is better.

---

# 9️⃣ ROC Curve

The **Receiver Operating Characteristic (ROC) Curve** shows how well a classifier separates positive and negative classes.

It plots:

- **True Positive Rate (Recall)** on the Y-axis
- **False Positive Rate** on the X-axis

A better classifier stays closer to the **top-left corner**.

---

# 🔟 AUC (Area Under the Curve)

AUC measures the area under the ROC curve.

It ranges from **0 to 1**.

| AUC | Interpretation |
|------|---------------|
| 1.0 | Perfect classifier |
| 0.9 | Excellent |
| 0.8 | Good |
| 0.7 | Fair |
| 0.5 | Random guessing |

Higher AUC means better class separation.

---

# 1️⃣1️⃣ Log Loss

Log Loss evaluates the quality of **predicted probabilities**, not just predicted classes.

A model is rewarded for being **confident and correct**.

It is penalized heavily for being **confident but wrong**.

Lower Log Loss is better.

---

# 1️⃣2️⃣ Matthews Correlation Coefficient (MCC)

MCC is one of the most reliable metrics for **imbalanced datasets**.

Unlike accuracy, it considers **all four values** in the confusion matrix:

- TP
- TN
- FP
- FN

Its value ranges from:

| MCC | Meaning |
|------|---------|
| +1 | Perfect prediction |
| 0 | Random prediction |
| -1 | Completely incorrect prediction |

---

# Which Metric Should You Use?

| Metric | Best For |
|---------|-----------|
| Accuracy | Balanced datasets |
| Precision | Avoiding false positives |
| Recall | Avoiding false negatives |
| Specificity | Detecting negative cases correctly |
| F1 Score | Balancing precision and recall |
| ROC-AUC | Comparing classifiers |
| Log Loss | Probability predictions |
| MCC | Imbalanced datasets |

---

# Summary

There is **no single "best" evaluation metric**.

The right metric depends on the problem you're solving:

- Use **Accuracy** for balanced datasets.
- Use **Precision** when false positives are costly.
- Use **Recall** when missing positive cases is dangerous.
- Use **F1 Score** when you need a balance between precision and recall.
- Use **ROC-AUC** to compare classification models.
- Use **MCC** for highly imbalanced datasets.

Understanding these metrics helps you choose the right model and make better decisions based on its performance.
