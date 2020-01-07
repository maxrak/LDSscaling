import pandas as pd
from pathlib import Path
from Plot import Plot
from costs import costs
from scalingPolicy import scalingPolicy

base_dir = str(Path().resolve())

names = ['Conf', 'profile', 'Cuser', 'rate', 'RT', 'KO', 'Nrequest', '%KO', 'RTStdDev']
ConfTable=['1WPmedium_1DBmedium ','2WPmedium_1DBmedium ','3WPmedium_1DBmedium ','1WPmedium_1DBlarge ','2WPmedium_1DBlarge ','3WPmedium_1DBlarge ']#,'1WPlarge_1DB ']
#ConfTable=['1WPmedium_1DBmedium ','2WPmedium_1DBmedium ','3WPmedium_1DBmedium ']
CostTable={'medium':0.0288,'large':0.0576,'xlarge':0.1152,'xxlarge':0.2304,'':0.2304}
Profiles=[' author ',' editor ',' shopmanager ', ' userreader ']
#Profiles=[' userreader ']

file = base_dir + '/data/stats.csv'

df = pd.read_csv(file, names=names, header=None)
costs = costs(CostTable)
plot = Plot(df, ConfTable, CostTable, Profiles,costs)
policy = scalingPolicy(df, ConfTable, CostTable, Profiles,costs)
plot.evaluate()
#policy.evaluate()

#print costs.costFromString('1WPmedium_1DBmedium')
