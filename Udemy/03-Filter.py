import pandas as pd

data = pd.read_csv("./Udemy/Data/sales.csv", index_col="State")
# print(data)

highest_sales = (data["Sales"] > 300)

# data_sales = data.loc[highest_sales, ["Product", "Inventory", "Sales"]]
data_sales = data.loc[highest_sales]

unique = data["Product"].unique() # this method get the unique value from "Products" column

product = ['Caffe Mocha', 'Caffe Latte', 'Green Tea']

product_filter = ~data["Product"].isin(product)
# print(product_filter)

data = data.loc[product_filter]

columns = data.columns

rows, cols = data.shape

print(data[columns[0]].iloc[1], " + ", data[columns[0]].iloc[2], " = ", data[columns[0]].iloc[1] + data[columns[0]].iloc[2])

print("rows: ", rows, "  cols: ", cols)
# print(data[columns["Total Expenses"]].iloc[1], " + ", data[columns["Total Expenses"]].iloc[2], " = ", data[columns["Total Expenses"]].iloc[1] + data[columns["Total Expenses"]].iloc[2])