from pandas import *
from numpy import *

# import the data
data_03 = read_csv('data_03.csv',dtype={'code_industry':str,'open_year':str})

# select the variables
data03 = data_03[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'fixasset_total','depreciation_year','tax_va','input','va']]
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