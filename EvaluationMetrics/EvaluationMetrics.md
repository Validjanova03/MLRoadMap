# 📊 Evaluation Metrics Deep Dive (NumPy Only)

This document explores core evaluation metrics for classification models, implemented **from scratch with NumPy**.

---

## 🔹 Confusion Matrix

The confusion matrix shows counts of **True Positives (TP), False Positives (FP), True Negatives (TN), False Negatives (FN)**.

```python
import numpy as np

def confusion_matrix(y_true, y_pred):
    classes = np.unique(np.concatenate((y_true, y_pred)))
    matrix = np.zeros((len(classes), len(classes)), dtype=int)
    for i, actual in enumerate(classes):
        for j, predicted in enumerate(classes):
            matrix[i, j] = np.sum((y_true == actual) & (y_pred == predicted))
    return matrix, classes

# Example
y_true = np.array([1,0,1,1,0,0,1])
y_pred = np.array([1,0,0,1,0,1,1])
cm, labels = confusion_matrix(y_true, y_pred)
print("Labels:", labels)
print(cm)
