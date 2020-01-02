import pandas as pd
from pathlib import Path
from Plot import Plot
from costs import costs

base_dir = str(Path().resolve())

names = ['Conf', 'profile', 'Cuser', 'rate', 'RT', 'KO', 'Nrequest', '%KO']
CostTable={'medium':0.0288,'large':0.0576,'xlarge':0.1152,'xxlarge':0.2304,' ':0.2304}
Conf=['1WPmedium_1DB ','2WPmedium_1DB ','3WPmedium_1DB ','1WPlarge_1DB ','1WPmedium_1DBmedium ','2WPmedium_1DBmedium ','3WPmedium_1DBmedium ']

file = base_dir + '/data/stats.csv'

df = pd.read_csv(file, names=names, header=None)

plot = Plot(df)
costs = costs(CostTable)
#plot.evaluate()
print costs.costFromString('1WPmedium_1DBmedium')
