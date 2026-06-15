import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([50,60,70,80,90])
model = LinearRegression()
model.fit(X,y)
predictions = model.predict(X)
print(f"Learned W: {model.coef_[0]} \nLearned B: {model.intercept_}")
print(f"R2 Score: {r2_score(y, predictions)}")


# Output is:
# Learned W: 9.999999999999998 
# Learned B: 40.00000000000001
# R2 Score: 1.0

