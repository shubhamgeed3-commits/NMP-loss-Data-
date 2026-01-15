import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("NMP Loss.xlsx")

df.dropna(inplace=True)

df = df.apply(pd.to_numeric, errors="ignore")

num_cols = df.select_dtypes(include="number").columns

df[num_cols] = df[num_cols].clip(lower=0)

df = df[(df != 0).all(axis=1)]

print(df)

target_col = num_cols[-1]   

for col in num_cols[:-1]:
    plt.figure()
    
    grouped = df.groupby(col)[target_col].mean().reset_index()
    
    plt.plot(grouped[col], grouped[target_col], marker='o')
    plt.title(f"Average Target NMP Loss vs {col}")
    plt.xlabel(col)
    plt.ylabel(target_col)
    plt.show()



