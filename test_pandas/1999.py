'''acquire the 1999 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_99 = read_stata('/media/xuliheng/1830A48430A46B08/industry/1999.dta')

# select the variables
data99 = data_99[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','employee','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input','code_post']]
del data_99

# create new variables
data99['year'] = 1999
data99['code_9803'] = data99.code_9803.apply(str)
f=lambda x: x[0:2]
data99['pro'] = data99.code_9803.apply(f)
data99['sic']= data99.code_industry.apply(str).apply(f)

# write data
data99.to_csv('data99.csv',index=False, index_label=False)
del data99