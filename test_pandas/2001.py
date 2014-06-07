'''acquire the 2001 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_01 = read_stata('/media/xuliheng/1830A48430A46B08/industry/2001.dta')

# select the variables
data01 = data_01[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','employee','output','export'
                ,'fixasset_total','depreciation_year','tax_va','input','code_post']]
del data_01

# create new variables
data01['va']=data01.output - data01.input + data01.tax_va
data01['year'] = 2001
data01['code_9803'] = data01.code_9803.apply(str)
f=lambda x: x[0:2]
data01['pro'] = data01.code_9803.apply(f)
data01['sic']= data01.code_industry.apply(str).apply(f)

# write data
data01.to_csv('data01.csv',index=False, index_label=False)
del data01