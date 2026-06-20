from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("agaricus-lepiota.data",header=None)
X = df.iloc[:,1:]
y = df.iloc[:,0]

for col in X.columns:
    X[col] = LabelEncoder().fit_transform(X[col])
y = LabelEncoder().fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tree = DecisionTreeClassifier(max_depth=3, random_state=42)
tree.fit(X_train, y_train)

acc_test = accuracy_score(y_test, tree.predict(X_test))
print("Test accuracy:" , acc_test)
plt.figure(figsize = (20,10))
plot_tree(tree,filled=True,rounded = True, fontsize = 10)
plt.show()











