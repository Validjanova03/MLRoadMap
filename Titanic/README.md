# Titanic Survival Prediction

My first end-to-end ML project. Built as part of my [30-day ML roadmap](../README.md).

**Val accuracy: 81% · Kaggle public score: 0.75358**

## What I did

- Exploratory Data Analysis (EDA) — survival rates by sex, class, age, embarked port
- Handled missing data — Age imputed with median, Cabin dropped (77% missing)
- Visualised distributions and correlations with matplotlib & seaborn
- Built a Logistic Regression pipeline with scikit-learn
- Evaluated with accuracy, precision, recall, F1-score, and confusion matrix
- Generated and submitted predictions to Kaggle

## Files

| File | Purpose |
|------|---------|
| `titanic_eda.py` | Data exploration and visualisation |
| `titanic_model.py` | Preprocessing, model training, evaluation |
| `titanic_kaggle_submission.py` | Final predictions → `submission.csv` |

## Setup

Download `train.csv` and `test.csv` from [Kaggle](https://www.kaggle.com/competitions/titanic/data) and place them in this folder.

```bash
pip install pandas numpy scikit-learn matplotlib seaborn

python titanic_eda.py
python titanic_model.py
python titanic_kaggle_submission.py
```
