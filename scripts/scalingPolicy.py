import numpy as np 
import pandas as pd
import costs as costs

class scalingPolicy():
	
	def __init__(self, df, ConfTable, CostTable, Profiles, costs):
		self.df = df
		self.Conf=ConfTable
		self.Costs=CostTable
		self.Profiles=Profiles
		self.costs = costs
		self.confs=self.analyze()

	def MAR(self, val,r,ko):
		mar=0
		#print "evaluating MAR "+str(val)+"%"
		for j in range(len(ko)):
			if (ko[j]<val) and (r[j]>mar):
				mar=r[j]
			#print "ko:"+str(ko[j])+" r:"+str(r[j])+"temp mar:"+str(mar)
		#print "MAR "+str(val)+"%="+str(mar)
		return mar

	def analyze(self):
		length=len(self.Conf)
		confs=[]
		for i in range(length):
			df2 = self.df.loc[(self.df['Conf'] == self.Conf[i])]
			r = df2['rate']
			ko = df2['%KO']
			r=r.values.tolist()
			ko=ko.values.tolist()
			#res=[self.Conf[i],[self.MAR(3,r,ko),self.MAR(5,r,ko),self.MAR(7,r,ko)],self.costs.costFromString(self.Conf[i])]
			mar5=self.MAR(5,r,ko)
			res=[self.Conf[i],[mar5*0.95,mar5,mar5*1.05],self.costs.costFromString(self.Conf[i])]			
			confs.append(res)
			#print res
		return confs

	def evaluate(self):
		policy=[]
		startconf=self.minForRate(0)
		policy.append(self.confs[startconf])
		nextrate=self.confs[startconf][1][1]*1.1
		maxmar=self.maxMAR()
		maxconf=self.minForRate(maxmar)
		while (nextrate<maxmar):
			nextconf=self.minForRate(nextrate)
			nextrate=self.confs[nextconf][1][1]*1.1
			policy.append(self.confs[nextconf])
		print policy
		return policy

	def minForRate(self,rate):
		acost=1000
		id=-1
		for i in range(len(self.confs)):
			if ((self.confs[i][2]<acost) and rate<self.confs[i][1][1]):
				id=i
				acost=self.confs[i][2]
		print self.confs[id][0]
		return id

	def maxMAR(self):
		mar=0
		for i in range(len(self.confs)):
			if (mar<self.confs[i][1][1]):
				mar=self.confs[i][1][1]
		print mar
		return mar