import pandas as pd

data = pd.read_csv("./Data/sales.csv")

new_column = data["Total Expenses"] + data["Sales"]

data["New Column"] = new_column # add a new column

data.drop(columns=['Marketing', 'Profit'], inplace=True) # remove a column spacefed

data.drop(index=0, inplace=True) # remove a row

print(data)