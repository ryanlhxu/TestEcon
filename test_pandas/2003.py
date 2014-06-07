'''acquire the 2003 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_03 = read_stata('/media/xuliheng/1830A48430A46B08/industry/2003.dta')

# select the variables
data03 = data_03[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'fixasset_total','depreciation_year','tax_va','input','va','code_post']]
del data_03

# create new variables
data03['year'] = 2003
data03['code_9803'] = data03.code_9803.apply(str)
f=lambda x: x[0:2]
data03['pro'] = data03.code_9803.apply(f)
data03['sic']= data03.code_industry.apply(str).apply(f)

# write data
data03.to_csv('data03.csv',index=False, index_label=False)
del data03