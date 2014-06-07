'''acquire the 2007 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_07 = read_stata('/media/xuliheng/1830A48430A46B08/industry/2007.dta')

# select the variables
data07 = data_07[["id","code_0409","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input','code_post']]
del data_07

# create new variables
data07['year'] = 2007
data07['code_0409'] = data07.code_0409.apply(str)
f=lambda x: x[0:2]
data07['pro'] = data07.code_0409.apply(f)
data07['sic']= data07.code_industry.apply(str).apply(f)

# write data
data07.to_csv('data07.csv',index=False, index_label=False)
del data07