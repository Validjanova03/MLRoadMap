from sklearn.linear_model import RidgeCV
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

alphas = np.logspace(-3, -3,50)
ridge = RidgeCV(alphas=alphas, cv=5)
ridge.fit(X_train,y_train)
print("Best Alpha:", ridge.alpha_)
print("R^2 on test set:", ridge.score(X_test,y_test))

