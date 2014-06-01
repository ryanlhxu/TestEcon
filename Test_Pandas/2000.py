from pandas import *
from numpy import *

# import the data
data_00 = read_csv('data_00.csv',dtype={'code_industry':str,'open_year':str})

# select the variables
data00 = data_00[["id","code_9803","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input']]
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