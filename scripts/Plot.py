import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import costs as costs
from scipy.interpolate import splrep, splev

from pathlib import Path
base_dir = str(Path().resolve())
colors=['bo','ro','go','mo','co','yo','ko']
colorsl=['b','r','g','m','c','y','k']
class Plot():

	def __init__(self, df, ConfTable, CostTable, Profiles, costs):
		self.df = df
		self.Conf=ConfTable
		self.Costs=CostTable
		self.Profiles=Profiles
		self.costs = costs

	def evaluate(self):
		length = len(self.Profiles)
		for i in range(length):
			self.plot_RT(self.Conf,self.Profiles[i], self.df)
			self.plot_Rate(self.Conf,self.Profiles[i], self.df)
			self.plot_KO(self.Conf,self.Profiles[i], self.df)
			self.plot_CostKuser(self.Conf,self.Profiles[i], self.df)
			self.plot_MAR(self.Conf,self.Profiles[i], self.df)


	def plot_RT(self, Conf, profile, df ):
		length = len(Conf)
		for i in range(length): 
			print "Plot RT for "+Conf[i]+" on"+profile
			df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
			z = df2['Cuser']
			h = df2['RT']
			#pd.to_numeric(df2['RT'])
			z = z.values.tolist()
			h = h.values.tolist()
			bspl1 = splrep(z, h, s=5)
			bspl_z = splev(z, bspl1)
			plt.plot(z, h, colors[i], label=Conf[i])
			plt.plot(z, bspl_z,colorsl[i])

		plt.legend(loc="upper left")
		plt.xlabel('Cuser')
		plt.ylabel('RT(ms)')
		plt.title(profile+' RT - measured')
		plt.savefig(base_dir + '/output/plot_'+profile.strip()+'RTMea.png', bbox_inches='tight', dpi=500)
		plt.clf()

	def plot_Rate(self, Conf, profile, df ):
		length = len(Conf)
		for i in range(length): 
			print "Plot Rate for "+Conf[i]+" on"+profile
			df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
			z = df2['Cuser']
			h = df2['rate']
			pd.to_numeric(df2['rate'])
			z = z.values.tolist()
			h = h.values.tolist()
			bspl1 = splrep(z, h, s=5)
			bspl_z = splev(z, bspl1)
			plt.plot(z, h, colors[i], label=Conf[i])
			plt.plot(z, bspl_z,colorsl[i])

		plt.legend(loc="upper left")
		plt.xlabel('Cuser')
		plt.ylabel('Rate (req/s)')
		plt.title(profile+' Rate required')
		plt.savefig(base_dir + '/output/plot_'+profile.strip()+'RateReq.png', bbox_inches='tight', dpi=500)
		plt.clf()

	def plot_KO(self, Conf, profile, df ):
		length = len(Conf)
		for i in range(length): 
			print "Plot KO for "+Conf[i]+" on"+profile
			df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
			z = df2['Cuser']
			h = df2['%KO']
			pd.to_numeric(df2['%KO'])
			z = z.values.tolist()
			h = h.values.tolist()
			bspl1 = splrep(z, h, s=5)
			bspl_z = splev(z, bspl1)
			plt.plot(z, h, colors[i], label=Conf[i])
			plt.plot(z, bspl_z,colorsl[i])

		plt.legend(loc="upper left")
		plt.xlabel('Cuser')
		plt.ylabel('Ko% ')
		plt.title(profile+' - KO%')
		plt.savefig(base_dir + '/output/plot_'+profile.strip()+'KO.png', bbox_inches='tight', dpi=500)
		plt.clf()

	def plot_CostKuser(self, Conf, profile, df ):
		length = len(Conf)
		for i in range(length): 
			print "Plot Cost per Kusers for "+Conf[i]+" on"+profile
			df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
			cost=self.costs.costFromString(Conf[i].strip())
			z = df2['Cuser']
			r = df2['rate']
			h = cost/(r*3.6)
			z = z.values.tolist()
			h = h.values.tolist()
			r = r.values.tolist()
			bspl1 = splrep(z, h, s=5)
			bspl_z = splev(z, bspl1)
			#bspl2 = splrep(r,h,s=5)
			#bspl_r2 = splev(r,bspl2)
			#plt.plot(z, h, colors[i], label=Conf[i])
			#plt.plot(z, bspl_z, colorsl[i], label=Conf[i])
			#plt.plot(r, h, colors[i], label=Conf[i])
			plt.plot(r, h, colorsl[i], label=Conf[i])

		plt.legend(loc="upper right")
		plt.xlabel('rate (Req/s)')
		plt.ylabel('Cost per K requests ')
		plt.title(profile+' - Cost per K requests')
		plt.savefig(base_dir + '/output/plot_'+profile.strip()+'cost.png', bbox_inches='tight', dpi=500)
		plt.clf()		

	def plot_MAR(self, Conf, profile, df ):
		length = len(Conf)
		mar5=[]
		for i in range(length): 
			print "Plot MAR for "+Conf[i]+" on"+profile
			df2 = df.loc[(df['Conf'] == Conf[i]) & (df['profile'] == profile)]
			r = df2['rate']
			ko = df2['%KO']
			r=r.values.tolist()
			ko=ko.values.tolist()
			mar5.append(r[0])
			for j in range(len(ko)):
				if ko[j]<5:
					mar5[i]=r[j]

		#w=3
		x_axis = np.arange(0, length)
		bar=plt.bar(x_axis,mar5)
		plt.xticks(x_axis+0.5,Conf,rotation='vertical');
		plt.ylabel('rate')
		for idx, rect in enumerate(bar):
			height=rect.get_height()
		 	plt.text(rect.get_x() + rect.get_width()/2., 1.05*height, round(mar5[idx],2), ha='center', va='bottom', rotation=0)
		plt.title(profile+' - MAR 5%')
		plt.savefig(base_dir + '/output/plot_'+profile.strip()+'MAR.png', bbox_inches='tight', dpi=500)
		plt.clf()

