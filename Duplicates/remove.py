import pandas as pd

fd = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data12.csv')


fd.drop_duplicates(inplace=True)

# as a result of the above statement, row 12 was removed


print(fd.to_string())