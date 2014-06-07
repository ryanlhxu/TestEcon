'''acquire the 1998 data
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# import the data
data_98 = read_stata('/media/xuliheng/1830A48430A46B08/industry/1998.dta')

# select the variables
data98 = data_98[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input','code_post']]
del data_98

# transfer open_year to int
data98['open_year'] = data98['open_year'].apply(int)


# create new variables
data98['year'] = 1998
data98['code_9803'] = data98.code_9803.apply(str)
f=lambda x: x[0:2]
data98['pro'] = data98.code_9803.apply(f)
data98['sic']= data98.code_industry.apply(str).apply(f)

# write data
data98.to_csv('data98.csv',index=False, index_label=False)
del data98


