import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

fd = pd.read_csv('C:\\Users\Jeremiah\\Documents\\CSV_files\\data1.csv')

fd.plot(kind = 'scatter', x = 'Time', y = 'Rate')

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()