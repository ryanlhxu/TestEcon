import os 
import numpy as np
import matplotlib.pylab as plt
import math

# HP filter of the data
# database is downloaded from perri's website

# set the working directory
os.chdir("/home/xuliheng/github/TestEcon/dsge")
os.getcwd()

# read csv data and convert it to ndarray
data_type="|S6,"+"<f8,"*10+"<f8"
data =np.genfromtxt('data.csv',dtype=data_type,delimiter=',',names=True)
print data.dtype.names
# GDP data
gdp = [math.log(i) for i in data["GDP"]]

# HP filter of GDP
import statsmodels.api as sm 
gdp_cycle, gdp_trend =sm.tsa.filters.hpfilter(gdp,1600)
plt.plot(gdp_cycle,'r-')
plt.show()
'''
plt.plot(gdp,'-r')
plt.plot(gdp_trend,'-b')
plt.xlabel('period')
plt.ylabel('log(GDP)')
plt.show()
'''
# std of GDP
gdp_std = np.std(gdp_cycle)
print gdp_std 
# filter of other variables
var_std = {}
var_std["GDP"]= gdp_std
var_corr = {}
# filter of other variables
for i in range(2,12):
    var_name = data.dtype.names[i]
    if var_name != "Net_Exports":
        var = [math.log(j) for j in data[var_name]]
    else:
	var = data[var_name]
    #debug
    #if i==2:
    #    print var_name
    var_cycle,var_trend = sm.tsa.filters.hpfilter(var,1600)
    var_corr[var_name] = np.corrcoef(gdp_cycle,var_cycle)[0][1]
    if var_name in ["Total_C","GFCF","Civilian_Emp"]:
        var_std[var_name]=np.std(var_cycle)/gdp_std      
        #if i==2:
        #   print var_std 
    else:
        var_std[var_name]=np.std(var_cycle)
print var_std 
print var_corr

across_corr={}
data2_type="|S6,"+"<f8,"*3+"<f8"
data2 =np.genfromtxt('data2.csv',dtype=data2_type,delimiter=',',names=True)
for i in range(1,5):
    var_name = data2.dtype.names[i]
    var_2 = [math.log(k) for k in data2[var_name]]
    var_1 = [math.log(k) for k in data[var_name]]
    var_1_cycle,var_1_trend = sm.tsa.filters.hpfilter(var_1,1600)
    var_2_cycle,var_2_trend = sm.tsa.filters.hpfilter(var_2,1600)
    across_corr[var_name]=np.corrcoef(var_1_cycle,var_2_cycle)[0][1]
print across_corr


    



