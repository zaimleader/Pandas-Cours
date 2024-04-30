import pandas as pd

data = pd.read_csv("./Udemy/Data/sales.csv")

# null_data = data.isnull().sum()

null_mask = data.isnull().all(axis=1)

# print(null_data)

print("\n")

print(null_mask)

print("\n")

# Filter the DataFrame to only include empty rows
null_rows = data[null_mask]

# Print the empty rows
print(null_rows)

data.dropna(inplace=True)

clean_null_data = data.isnull().sum()

# print(clean_null_data)