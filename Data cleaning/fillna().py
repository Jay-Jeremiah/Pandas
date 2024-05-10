# fillna() attribute allows one to replace NUll values

import pandas as pd

df = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data5.csv')

df.fillna(130, inplace = True)

print(df.to_string())

# fillna() can also be used to replace NULL values in a specified row column in a dataframe

df