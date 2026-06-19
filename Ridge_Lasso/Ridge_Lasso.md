# Regularization: Ridge & Lasso

Our model learned **TOO HARD**. It memorized the training data, including its noise and now fails on new data.

Without Regularization: Weights grow freely to fit every data point.

Regularization - used to prevent overfitting by adding a penalty term to the loss function.

## 1) Ridge (L2)

Weight shrink toward 0 but never reach it.

**RIDGE MSE = MSE + λ * Σ(w²)**

Penalises big weights.

**Lambda (λ)**

How hard you penalise.

* λ = 0 means no penalty ("normal regression")
* Large λ means very aggressive shrinkage

### Characteristics

* Penalises w² (squaring)
* Shrinks weight toward 0
* Never fully removes a feature
* Keeps all features in model
* Good when all features matter a little

### USE RIDGE WHEN...

* Want to keep all features but reduce impact
* Example: Predict Salary → Age, Experience, Education all matter

---

## 2) Lasso (L1)

Weak weights get eliminated, set exactly 0.

**LASSO MSE = MSE + λ * Σ|w|**

Penalises any weight.

### Characteristics

* Penalises |w| (absolute value)
* Does automatic feature selection
* Produces sparse models (lots of zeros)
* Good when most features are irrelevant

### USE LASSO WHEN...

* You have many features and suspect most are irrelevant
* Want a simpler, interpretable model
* Example: Gene Expression data → 10,000 genes, only 20 matter

---

## 3) ElasticNet

Mix of both Ridge and Lasso.

**ELASTICNET MSE = MSE + λ₁ * Σ(w²) + λ₂ * Σ|w|**

Best of both worlds.

When you want some features eliminated (Lasso) but also want stability (Ridge).

---

## Quick Rule

* Few features, all likely useful → **RIDGE**
* Many features, most likely noise → **LASSO**
* Unsure → **ELASTICNET** or **TRY BOTH**
* Not sure if you even need regularization → **CHECK IF TRAIN ACCURACY > TEST ACCURACY**
