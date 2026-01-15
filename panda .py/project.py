import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("NMP loss.xlsx")

df.dropna(inplace=True)

df = df.apply(pd.to_numeric, errors="ignore")

num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].clip(lower=0)

df = df[(df != 0).all(axis=1)]

print(df.to_string())

target_column = "Target NMP loss "

y = df[target_column]
X = df.drop(columns=[target_column])

print(df.columns.tolist())

plt.plot()
plt.title("Target NMP Loss")
plt.xlabel("Index")
plt.ylabel("Target NMP Loss")
plt.show()
