import numpy as np
from sklearn.metrics import r2_score

X = np.array([1,2,3,4,5])
y = np.array([50,60,70,80,90])

w=0 
b=0
learining_rate = 0.01
epochs = 1000

n = len(X)
for _ in range(epochs):
    y_pred = w*X + b
    dw = (-2/n) * sum(X * (y - y_pred))
    db = (-2/n) * sum(y - y_pred)
    
    w = w - learining_rate * dw
    b = b - learining_rate * db
print(f"Learned W: {w} \nLearned B: {b}")
predictions = w*X + b
print("R2 Score:",round(r2_score(y,predictions),4))

"""
Output is: 
Learned W: 10.3239110201721 
Learned B: 38.830578440768576
R2 Score: 0.9988
"""
