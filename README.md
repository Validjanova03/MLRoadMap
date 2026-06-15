# ML Roadmap

Documenting my 30-day journey to junior ML engineer level — one project at a time.

## Structure

```
MLRoadMap/
├── ScikitLearn/
│   ├── iris_classification.py     ← 3-model comparison on Iris
│   ├── overfitting_demo.py        ← Visualising overfitting vs underfitting
│   └── bias_variance_notes.md     ← Personal notes on the tradeoff
│
└── Titanic/
│   ├── titanic_eda.py             ← EDA and visualisation
│   ├── titanic_model.py           ← Logistic Regression, evaluation
│   └── titanic_kaggle_submission.py ← Final predictions + CSV
├── Notes/
│   ├── supervised_vs_unsupervised.md    ← Key differences and examples
│   └──  ml_glossary.md                  ← Important ML terminology
├── LinearRegression/
│   ├── linear_regression_from_scratch.py
│   ├── linear_regression_sklearn.py
│   ├── gradient_descent_demo.py
│   └── linear_regression_notes.md
```

## Progress

| Week | Focus | Status |
|------|-------|--------|
| 1 | Probability, ML basics, sklearn fundamentals |  Done |
| 2 | Linear Regression, Decision Trees, Titanic project |  Done |
| 3 | SVM, Naive Bayes, kNN, Neural Nets, Pipelines |  In progress |
| 4 | Feature engineering, portfolio polish, mock interviews |  Upcoming |

## Projects

**ScikitLearn/** — foundations: classification, overfitting, bias-variance tradeoff.

**Titanic/** — first end-to-end ML project. EDA → preprocessing → Logistic Regression → Kaggle submission. **Val accuracy: 81% · Kaggle score: 0.75358** → [details](./Titanic/README.md)

## Setup

```bash
git clone https://github.com/Validjanova03/MLRoadMap.git
cd MLRoadMap
pip install -r requirements.txt
```
## Stack

`Python` · `scikit-learn` · `pandas` · `numpy` · `matplotlib` · `seaborn`
