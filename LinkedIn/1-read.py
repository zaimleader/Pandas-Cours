import pandas as pd 
from openpyxl.workbook import Workbook

import os

path = "Python/Pandas/resources/"

path = os.path.join(os.getcwd(), "LinkedIn/resources/excel")

path_file = os.path.join(path, "GDM_AIS_R1_OFFI___ECR-ECO_W14.xlsx")


df_xlsx = pd.read_excel(path_file)

df_xlsx = pd.ExcelFile(path_file)
# df_csv = pd.read_csv(path + "excel/crime.csv")
# df_txt = pd.read_csv(path + "files/data.txt", delimiter="\t")

print(df_xlsx)
print("\n")
print(df_xlsx.columns)