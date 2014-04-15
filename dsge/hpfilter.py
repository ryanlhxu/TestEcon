import os 
import numpy as np
import matplotlib.pylab as plt

# HP filter of the data
# database is downloaded from perri's website

# set the working directory
os.chdir("c:/Users/xuliheng/documents/github/TestEcon/dsge")
os.getcwd()

# read csv data and convert it to ndarray
data_type="|S6,"+"<f8,"*10+"<f8"
data =np.genfromtxt('data.csv',dtype=data_type,delimiter=',',names=True)

# GDP data
gdp = data["GDP"]

# HP filter of GDP
import statsmodels.api as sm 
gdp_cycle, gdp_trend =sm.tsa.filters.hpfilter(gdp,1600)

plt.plot(gdp,'-r')
plt.plot(gdp_trend,'-b')
plt.show()

# std of GDP
gdp_std = np.std(gdp_cycle/gdp_trend)
 
# filter of other variables
t =  data.shape[0]
cycle = np.zeros(t)
trend = np.zeros(t)
var_std = []
var_std.append(gdp_std)

# filter of other variables
for i in range(2,12):
    var_name = data.dtype.names[i]
    var = data[var_name]
    #debug
    #if i==2:
    #    print var_name
    cycle,trend = sm.tsa.filters.hpfilter(var,1600)
    if var_name in ["Total_C","GFCF","Civilian_Emp"]:
        var_std.append(np.std(cycle/trend)/gdp_std)
        # dubug
        #if i==2:
        #   print var_std 
    else:
        var_std.append(np.std(cycle/trend)) 
        


  





