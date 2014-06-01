from pandas import *
from numpy import *

# import the data
data_06 = read_csv('data_06.csv',dtype={'code_industry':str,'open_year':str})

# select the variables
data06 = data_06[["id","code_0409","code_industry",'type_reg','type_stateowned','open_year','worker','output','export'
                ,'va','fixasset_total','depreciation_year','tax_va','input']]
del data_06

# create new variables
data06['year'] = 2006
data06['code_0409'] = data06.code_0409.apply(str)
f=lambda x: x[0:2]
data06['pro'] = data06.code_0409.apply(f)
data06['sic']= data06.code_industry.apply(str).apply(f)

# write data
data06.to_csv('data06.csv',index=False, index_label=False)
del data06