import numpy as np
from matplotlib.pylab import plt   
data_type = "<f8"
data =np.genfromtxt('f2011.csv',dtype=data_type,delimiter=',',names=True)
wage=data['ws']
p1=plt.hist(wage,bins=1000, histtype='step',color='b',normed=1)
plt.ylabel("")
plt.xlabel("Monthly Earnings")
plt.xlim(0,15000)
plt.show()