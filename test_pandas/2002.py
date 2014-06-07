'''acquire the 2001 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_02 = read_stata('/media/xuliheng/1830A48430A46B08/industry/2002.dta')

# select the variables
data02 = data_02[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','employee','output','export'
                ,'fixasset_total','depreciation_year','tax_va','input','va','code_post']]
del data_02

# create new variables
data02['year'] = 2002
data02['code_9803'] = data02.code_9803.apply(str)
f=lambda x: x[0:2]
data02['pro'] = data02.code_9803.apply(f)
data02['sic']= data02.code_industry.apply(str).apply(f)

# write data
data02.to_csv('data02.csv',index=False, index_label=False)
del data02