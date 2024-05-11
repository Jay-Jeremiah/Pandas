# mode() helps to calculate mode in a data set

import pandas as pd

ab = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data5.csv')

x = ab["Duration"].mode()

print(x)