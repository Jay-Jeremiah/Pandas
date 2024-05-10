# fillna() attribute is also used to repalce Null values 
# in a specified column in a dataframe

import pandas as pd

df = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data5.csv')

df["Calories"].fillna(130, inplace= True)

print(df.to_string())