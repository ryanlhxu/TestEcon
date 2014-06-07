'''acquire the 2004 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_04 = read_stata('/media/xuliheng/1830A48430A46B08/industry/2004.dta')

# select the variables
data04 = data_04[["id","code_0409","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'fixasset_total','depreciation_year','tax_va','input','code_post']]
del data_04

# create new variables
data04['va'] = data04.output - data04.input + data04.tax_va
data04['year'] = 2004
data04['code_0409'] = data04.code_0409.apply(str)
f=lambda x: x[0:2]
data04['pro'] = data04.code_0409.apply(f)
data04['sic']= data04.code_industry.apply(str).apply(f)

# write data
data04.to_csv('data04.csv',index=False, index_label=False)
del data04