import pandas as pd


fd = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data10.csv')

for x in fd.index:
    if fd.loc[x, "Calories"] > 120:
        fd.drop(x, inplace=True)

print(fd.to_string())

