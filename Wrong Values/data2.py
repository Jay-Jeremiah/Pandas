# replacing values in loops
import pandas as pd 

jf = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data9.csv')

for x in jf.index:
    if jf.loc[x, 'Duration'] > 120:
        jf.loc[x, 'Duration'] = 120

print(jf.to_string())