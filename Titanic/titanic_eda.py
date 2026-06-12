import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
print("First 5 Rows:")
print(df.head())

print("\nData Shape:")
print(df.shape)

print("\nData Info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# Histograms
df.hist(figsize = (12,8))
plt.tight_layout()
plt.show()

# Correlation Matrix
numeric_df= df.select_dtypes(include="number")
corr = numeric_df.corr()

print("\nCorrelation Matrix:")
print(corr)

df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Counts")
plt.show()

df["Age"].hist(bins = 20)
plt.title("Age Distribution")
plt.show()
