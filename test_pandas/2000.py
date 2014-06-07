'''acquire the 2000 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_00 = read_stata('/media/xuliheng/1830A48430A46B08/industry/2000.dta')

# select the variables
data00 = data_00[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input','code_post']]
del data_00

# create new variables
data00['year'] = 2000
data00['code_9803'] = data00.code_9803.apply(str)
f=lambda x: x[0:2]
data00['pro'] = data00.code_9803.apply(f)
data00['sic']= data00.code_industry.apply(str).apply(f)

# write data
data00.to_csv('data00.csv',index=False, index_label=False)
del data00