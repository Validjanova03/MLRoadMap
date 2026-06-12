import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import r2_score

np.random.seed(42)

X=np.linspace(-3, 3, 30).reshape(-1, 1)

y = X.ravel()**2 + np.random.normal(0,1,30)

X_train,X_test,y_train,y_test = train_test_split(X,y, test_size =0.4, random_state=42)


overfit_model = make_pipeline(
    PolynomialFeatures(degree=10),
    LinearRegression()
)

overfit_model.fit(X_train,y_train)

train_pred= overfit_model.predict(X_train)
test_pred= overfit_model.predict(X_test)

print("=== Overfitting Model ===")
print("Train R2:", round(r2_score(y_train, train_pred), 3))
print("Test R2:", round(r2_score(y_test, test_pred), 3))

# Regularized Model
ridge_model = make_pipeline(
    PolynomialFeatures(degree=10),
    Ridge(alpha=10.0)
)

ridge_model.fit(X_train, y_train)
train_pred_ridge = ridge_model.predict(X_train)
test_pred_ridge = ridge_model.predict(X_test)

print("\n=== Ridge Regularized Model ===")
print("Train R2:", round(r2_score(y_train, train_pred_ridge), 3))
print("Test R2:", round(r2_score(y_test, test_pred_ridge), 3))

# Plot
X_plot= np.linspace(-3, 3, 300).reshape(-1, 1)
y_overfit=overfit_model.predict(X_plot)
y_ridge=ridge_model.predict(X_plot)

plt.scatter(X_train, y_train, label="Train Data")
plt.scatter(X_test,y_test, label="Test Data")

plt.plot(X_plot,y_overfit,label="Overfit Degree = 20")
plt.plot(X_plot,y_ridge,label = "Ridge Degree=20")

plt.legend()
plt.title("Overfitting vs Ridge Regularization")
plt.show()
