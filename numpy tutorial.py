# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel("NMP Loss.xlsx")
# df.dropna(inplace=True)

# df = df.apply(pd.to_numeric, errors="ignore")
# num_cols = df.select_dtypes(include="number").columns
# df[num_cols] = df[num_cols].clip(lower=0)
# df = df[(df != 0).all(axis=1)]

# df.columns = df.columns.str.strip()

# print(df)
# print("COLUMNS:", list(df.columns))

# x_col = num_cols[0]
# y_col = "Target NMP loss"  
 
# plt.figure()
# plt.scatter(df[x_col], df[y_col])
# plt.title("Target NMP Loss")
# plt.xlabel(x_col)
# plt.ylabel(y_col)
# plt.

# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])
# print(arr.shape)   # (6,)
