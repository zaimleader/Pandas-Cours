import pandas as pd
import os

path = os.getcwd()
full_path = os.path.join(path, "Udemy/Data", "sales.csv")

data = pd.read_csv(full_path, index_col="State")

head = data.head() # head() mathod return 5 first data from my csv file if 
                   # if you want to see a certain numbers of rows you can pass a number on head(nbm_rows) method 
                   # like head(10) => 10 rows

tail = data.tail() # tail != head -> display 5 last data 

shape = data.shape # return number of rows & columns 

print(shape)