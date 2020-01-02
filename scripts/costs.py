class costs():
	def __init__(self, CostTable):
		self.CostTable = CostTable
	
	def confConverter(self, Configuration):
		types=Configuration.split("_")
		nWP=types[0][0]
		fWP=types[0][3:]
		nDB=types[1][0]
		fDB=types[1][3:]
		return [nWP,fWP,nDB,fDB]

	def cost(self, ConfVector):
		cWP=float(ConfVector[0])*float(self.CostTable[ConfVector[1]])
		cDB=float(ConfVector[2])*float(self.CostTable[ConfVector[3]])
		return cWP+cDB

	def costFromString(self, Config):
		#print Config
		confvector=self.confConverter(Config)
		return self.cost(confvector)
#conf=confConverter(Conf[0])
#print conf
#print cost(conf) 
