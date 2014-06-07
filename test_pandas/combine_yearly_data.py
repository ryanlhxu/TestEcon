''' combine the data from 1998 to 2007
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')


data98 = read_csv('data98.csv',dtype={'code_industry':str,"sic":str})
data98 = data98.rename(columns = {'code_9803':'code_pro','worker':'labor'})

data99 = read_csv('data99.csv',dtype={'code_industry':str,"sic":str})
data99 = data99.rename(columns = {'code_9803':'code_pro','employee':'labor'})

temp1 = concat([data98,data99],ignore_index=True)
del data98, data99

###################################################################################
data00 = read_csv('data00.csv',dtype={'code_industry':str,"sic":str})
data00= data00.rename(columns = {'code_9803':'code_pro','worker':'labor'})

temp2 = concat([temp1,data00],ignore_index=True)
del data00, temp1

####################################################################################
data01 = read_csv('data01.csv',dtype={'code_industry':str,"sic":str})
data01= data01.rename(columns = {'code_9803':'code_pro','employee':'labor'})

temp3 = concat([temp2,data01],ignore_index=True)
del data01, temp2

#######################################################################################
data02 = read_csv('data02.csv',dtype={'code_industry':str,"sic":str})
data02 = data02.rename(columns = {'code_9803':'code_pro','employee':'labor'})
temp4 = concat([temp3,data02],ignore_index=True)

temp4.to_csv('temp4.csv',index=False, index_label=False)
del data02, temp3


######################################################################################
data03 = read_csv('data03.csv',dtype={'code_industry':str,"sic":str})
data03 = data03.rename(columns = {'code_9803':'code_pro','worker':'labor'})
temp5 = concat([temp4,data03],ignore_index=True)
del data03, temp4

data04 = read_csv('data04.csv',dtype={'code_industry':str,"sic":str})
data04 = data04.rename(columns = {'code_0409':'code_pro','worker':'labor'})
temp6 = concat([temp5,data04],ignore_index=True)
del data04, temp5

data05 = read_csv('data05.csv',dtype={'code_industry':str,"sic":str})
data05 = data05.rename(columns = {'code_0409':'code_pro','worker':'labor'})
temp7 = concat([temp6,data05],ignore_index=True)
del data05, temp6

data06 = read_csv('data06.csv',dtype={'code_industry':str,"sic":str})
data06 = data06.rename(columns = {'code_0409':'code_pro','worker':'labor'})
temp8 = concat([temp7,data06],ignore_index=True)
del data06, temp7

data07 = read_csv('data07.csv',dtype={'code_industry':str,"sic":str})
data07 = data07.rename(columns = {'code_0409':'code_pro','worker':'labor'})
temp9 = concat([temp8,data07],ignore_index=True)
del data07
temp9.to_csv('combine_yearly_data.csv',index=False, index_label=False)
del temp9, temp8














