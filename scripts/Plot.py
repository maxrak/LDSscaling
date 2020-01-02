import matplotlib.pyplot as plt
import pandas as pd
import costs as costs
from scipy.interpolate import splrep, splev

from pathlib import Path
base_dir = str(Path().resolve())
Conf=['1WPmedium_1DB ','2WPmedium_1DB ','3WPmedium_1DB ','1WPlarge_1DB ','1WPmedium_1DBmedium ','2WPmedium_1DBmedium ','3WPmedium_1DBmedium ']
CostTable={'medium':0.0288,'large':0.0576,'xlarge':0.1152,'xxlarge':0.2304,' ':0.2304}
colors=['bo','ro','go','mo','co','yo','ko']
class Plot():

    def __init__(self, df):
        self.df = df

    def evaluate(self, auth=True, edit=True, shop=True):

        if auth:
            plot_RT(Conf,' author ', self.df)
            plot_Rate(Conf,' author ', self.df)
            plot_KO(Conf,' author ', self.df)

        if edit:
            plot_RT(Conf,' editor ', self.df)
            plot_Rate(Conf,' editor ', self.df)
            plot_KO(Conf,' editor ', self.df)

        if shop:
            plot_RT(Conf,' shopmanager ', self.df)
            plot_Rate(Conf,' shopmanager ', self.df)
            plot_KO(Conf,' shopmanager ', self.df)


def plot_RT(Conf, profile, df ):
    length = len(Conf)
    for i in range(length): 
        df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
        z = df2['Cuser']
        h = df2['RT']
        pd.to_numeric(df2['RT'])
        z = z.values.tolist()
        h = h.values.tolist()
        bspl1 = splrep(z, h, s=5)
        bspl_z = splev(z, bspl1)
        plt.plot(z, h, colors[i], label=Conf[i])
        plt.plot(z, bspl_z)

    plt.legend(loc="upper left")
    plt.xlabel('Cuser')
    plt.ylabel('RT(ms)')
    plt.title(profile+' RT - measured')
    plt.savefig(base_dir + '/output/plot_'+profile.strip()+'RTMea.png', bbox_inches='tight', dpi=500)
    plt.clf()

def plot_Rate(Conf, profile, df ):
    length = len(Conf)
    for i in range(length): 
        df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
        z = df2['Cuser']
        h = df2['rate']
        pd.to_numeric(df2['rate'])
        z = z.values.tolist()
        h = h.values.tolist()
        bspl1 = splrep(z, h, s=5)
        bspl_z = splev(z, bspl1)
        plt.plot(z, h, colors[i], label=Conf[i])
        plt.plot(z, bspl_z)

    plt.legend(loc="upper left")
    plt.xlabel('Cuser')
    plt.ylabel('Rate (req/s)')
    plt.title(profile+' Rate required')
    plt.savefig(base_dir + '/output/plot_'+profile.strip()+'RateReq.png', bbox_inches='tight', dpi=500)
    plt.clf()

def plot_KO(Conf, profile, df ):
    length = len(Conf)
    for i in range(length): 
        df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
        z = df2['Cuser']
        h = df2['%KO']
        pd.to_numeric(df2['KO'])
        z = z.values.tolist()
        h = h.values.tolist()
        bspl1 = splrep(z, h, s=5)
        bspl_z = splev(z, bspl1)
        plt.plot(z, h, colors[i], label=Conf[i])
        plt.plot(z, bspl_z)

    plt.legend(loc="upper left")
    plt.xlabel('Cuser')
    plt.ylabel('Ko% ')
    plt.title(profile+' - KO%')
    plt.savefig(base_dir + '/output/plot_'+profile.strip()+'KO.png', bbox_inches='tight', dpi=500)
    plt.clf()

