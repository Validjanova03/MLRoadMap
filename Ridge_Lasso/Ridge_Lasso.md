Regularization: Ridge & Lasso
Our model learned TOO HARD. It memorized the training data, including its noise and now fails on new data.
Without Regularization: Weights grow freely to fit every data point
Regularization - used to prevent overfitting by adding a penalty term to the loss function.
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
- You have many features and suspect most are irrelevant
- Want simpler, interpretable model
- Example: Gene Expression data - 10000 genes, only 20 metter

ElasticNet - Mix of both
ELASTICNET MSE = MSE + lambda1 * Sum(w^2) + lambda2 * Sum|w|
Best of both worlds. When you want some feature elaminated (Lasso) but also want stability (Ridge).

Few features, all likely useful -> RIDGE
Many features, most likely noise -> LASSO
Unsure -> ELASTICNET or TRY BOTH
Not sure if you even need regularization -> CHECK IF TRAIN > TEST ACCURACY


