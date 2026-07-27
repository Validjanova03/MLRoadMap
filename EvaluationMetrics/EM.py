# evaluation_metrics.py
# NumPy-only implementations of confusion matrix, precision, recall, F1, ROC curve, and AUC

import numpy as np
//ooi
def confusion_matrix(y_true, y_pred):
    classes = np.unique(np.concatenate((y_true, y_pred)))
    matrix = np.zeros((len(classes), len(classes)), dtype=int)
    for i, actual in enumerate(classes):
        for j, predicted in enumerate(classes):
            matrix[i, j] = np.sum((y_true == actual) & (y_pred == predicted))
    return matrix, classes

def precision_recall_f1(y_true, y_pred, positive_label=1):
    tp = np.sum((y_true == positive_label) & (y_pred == positive_label))
    fp = np.sum((y_true != positive_label) & (y_pred == positive_label))
    fn = np.sum((y_true == positive_label) & (y_pred != positive_label))

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, f1

def roc_curve(y_true, y_scores, positive_label=1):
    thresholds = np.sort(np.unique(y_scores))[::-1]
    tpr_list, fpr_list = [], []
    P = np.sum(y_true == positive_label)
    N = np.sum(y_true != positive_label)

    for thresh in thresholds:
        y_pred = (y_scores >= thresh).astype(int)
        tp = np.sum((y_true == positive_label) & (y_pred == positive_label))
        fp = np.sum((y_true != positive_label) & (y_pred == positive_label))

        tpr = tp / P if P > 0 else 0
        fpr = fp / N if N > 0 else 0
        tpr_list.append(tpr)
        fpr_list.append(fpr)

    return np.array(fpr_list), np.array(tpr_list), thresholds

def auc(fpr, tpr):
    return np.trapz(tpr, fpr)  # trapezoidal rule

# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    y_true = np.array([1,0,1,1,0,0,1])
    y_pred = np.array([1,0,0,1,0,1,1])
    y_scores = np.array([0.9,0.2,0.3,0.8,0.1,0.6,0.7])

    # Confusion Matrix
    cm, labels = confusion_matrix(y_true, y_pred)
    print("Labels:", labels)
    print("Confusion Matrix:\n", cm)

    # Precision, Recall, F1
    p, r, f1 = precision_recall_f1(y_true, y_pred)
    print(f"Precision={p:.3f}, Recall={r:.3f}, F1={f1:.3f}")

    # ROC Curve & AUC
    fpr, tpr, thresholds = roc_curve(y_true, y_scores)
    roc_auc = auc(fpr, tpr)
    print("FPR:", fpr)
    print("TPR:", tpr)
    print("Thresholds:", thresholds)
    print("ROC-AUC:", roc_auc)
