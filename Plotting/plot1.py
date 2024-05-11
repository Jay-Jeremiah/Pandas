import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

fd = pd.read_csv('C:\\Users\\Jeremiah\\Documents\\CSV_files\\data1.csv')

fd.plot()

plt.show()


# these two lines make the compiler able to draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()