import pandas as pd

data = pd.read_csv("./Data/sales.csv")

data_sort_val = data.sort_values("Total Expenses", ascending=False)

data_sort_ind = data.sort_index(ascending=False)

data_sort_col = data["Inventory"].sort_values(ascending=False)

print(data_sort_col)