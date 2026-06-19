Regularization: Ridge & Lasso
Our model learned TOO HARD. It memorized the training data, including its noise and now fails on new data.
Without Regularization: Weights grow freely to fit every data point

1) Ridge(L2) = weight shrink toward 0 but never reach it 
RIDGE MSE = MSE + lambda * Sum(w^2)  - Penalises big w

(lambda - How hard you penalise, lambda = 0 means no panalty "normal regression". Large lambda means very aggressive shrinkage.)
* Penalises w^2 - squaring
* Shrinks weight toward 0
* Never fully removes a feature
* Keeps all features in model
* Good when all features metter a little
USE RIDGE WHEN...
- Want keep all features but reduce impact
- Example: Predict Salary - Age, Experience, Education all metter

Lasso = Weak weights get eliminated, set exactly 0
LASSO MSE = MSE + lambda * Sum|w| - Penalises any w
* Penalises |w| - absolute value
* Does automatic feature selection
* Produces sparase models (lots of zeros)
* Good when most features are irrelevant
USE LASSO WHEN ...
