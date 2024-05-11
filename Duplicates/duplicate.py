# to discover duplicates in a data set, we use the duplicated() atrribute
# It returns booleans values for each value

import pandas as pd

fd = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data11.csv')

print(fd.duplicated())