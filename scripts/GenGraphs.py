import pandas as pd
from pathlib import Path
from Plot import Plot


base_dir = str(Path().resolve())

names = ['Conf', 'profile', 'Cuser', 'rate', 'RT', 'KO', 'Nrequest', '%KO']

file = base_dir + '/data/stats.csv'

df = pd.read_csv(file, names=names, header=None)


plot = Plot(df)

plot.evaluate()
