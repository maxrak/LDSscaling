import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

a=pd.read_csv('data/stats.csv', header=None, usecols=[2,6])
plt.figure()
rate=a.iloc[:25]
rate.plot()
plt.show()