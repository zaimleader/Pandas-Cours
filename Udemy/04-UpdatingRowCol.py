import pandas as pd

data = pd.read_csv("./Data/sales.csv")

columns_name = data.columns # return list of columns name 

data.columns = data.columns.str.replace(" ", "_") # replace space with _

data.rename(columns={"Total_Expenses": "Total_Exp"}, inplace=True) # rename column

# data.loc[2, "Total_Exp"] = 1000 # replace (row, col) value by another value

data.at[2, "Total_Exp"] = 5100 # another method

print(data.head())
