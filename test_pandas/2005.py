from pandas import *
from numpy import *

# import the data
data_05 = read_csv('data_05.csv',dtype={'code_industry':str,'open_year':str})

# select the variables
data05 = data_05[["id","code_0409","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input']]
del data_05

# create new variables
data05['year'] = 2005
data05['code_0409'] = data05.code_0409.apply(str)
f=lambda x: x[0:2]
data05['pro'] = data05.code_0409.apply(f)
data05['sic']= data05.code_industry.apply(str).apply(f)

# write data
data05.to_csv('data05.csv',index=False, index_label=False)
del data05