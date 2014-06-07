'''Aquire Balanced and Unbalanced Panel Data from the China's Manufacturing Database 
'''

from pandas import *
from numpy import *
import os

# set working directory 
os.chdir('/media/xuliheng/1830A48430A46B08/PythonFiles/tfp/')

# read the data
combine_yearly_data = read_csv('combine_yearly_data.csv',dtype={'code_industry':str,"sic":str})
panel = combine_yearly_data[['id','year','sic','pro','code_post']]
del combine_yearly_data

# order the data by id and year
panel_sheet = panel.sort(['id','year'],ascending=True).reset_index()
del panel_sheet['index'], panel 

# find naN of sic 
## na_sic = panel.id[isnull(panel['sic'])]
## 172435924: 08, 176882967:44, 17243610X:34; both in 2001
panel_sheet.sic[(panel_sheet.id == '172435924') & (panel_sheet.year==2001)]= '08'
panel_sheet.sic[(panel_sheet.id == '176882967') & (panel_sheet.year==2001)] = '44'
panel_sheet.sic[(panel_sheet.id == '17243610X') & (panel_sheet.year==2001)]  = '34'

# find NaN of pro
##na_pro= panel_sheet.id[isnull(panel_sheet['pro'])]
## 201602163:13, HA083489X:12; both in 2002
panel_sheet.pro[(panel_sheet.id == '201602163') & (panel_sheet.year==2002)]= '13'
panel_sheet.pro[(panel_sheet.id == 'HA083489X') & (panel_sheet.year==2002)]= '12'
panel_sheet.save('panel_sheet')
del panel_sheet

# deal with id which is not unique
panel_sheet = load('panel_sheet')
panel_sheet_id_year = panel_sheet.groupby(['id','year'])['code_post'].size()
panel_sheet_multi_id = panel_sheet_id_year[panel_sheet_id_year > 1].reset_index('year').index

# select the id which is unique in each year
panel_sheet_multi = panel_sheet[panel_sheet.id.isin(panel_sheet_multi_id)]
panel_sheet_unique = panel_sheet[-panel_sheet.id.isin(panel_sheet_multi_id)]
panel_sheet_unique.save('panel_sheet_unique')
panel_sheet_multi.save('panel_sheet_multi')
del panel_sheet_multi
del panel_sheet_unique

# acquire one-year sheet from the unique sheet
panel_sheet_unique = load('panel_sheet_unique')
length_year = (panel_sheet_unique.groupby('id')['year'].size())
one_year_sheet = panel_sheet_unique[panel_sheet_unique.id.isin(length_year.index[length_year==1])]
one_year_sheet.to_csv('one_year_sheet.csv',index=False, index_label=False)
del one_year_sheet

# multi_year_sheet from the unique sheet
multi_year_sheet = panel_sheet_unique[-panel_sheet_unique.id.isin(length_year.index[length_year==1])]
del length_year

# balanced panel sheet from the multi_year_sheet
total_year = 2007-1998+1
length_year =  (multi_year_sheet.groupby('id')['year'].size())
balanced_panel_sheet = multi_year_sheet[multi_year_sheet.id.isin(length_year.index[length_year==total_year])]
balanced_panel_sheet.to_csv('balanced_panel_sheet.csv',index=False, index_label=False)
del balanced_panel_sheet

# acquire the unbalanced panel which needs to deal with
ub_panel_sheet = multi_year_sheet[-multi_year_sheet.id.isin(length_year.index[length_year==total_year])]
del multi_year_sheet

# acquire the unbalanced panel which need not be delt with
ub_gap_year = ub_panel_sheet.groupby('id')['year'].apply(max)-ub_panel_sheet.groupby('id')['year'].apply(min)+1
ub_length_year = ub_panel_sheet.groupby('id')['year'].size()
ub_panel1_sheet=ub_panel_sheet[ub_panel_sheet.id.isin(ub_length_year.index[ub_length_year==ub_gap_year])]
ub_panel1_sheet.to_csv('ub_panel1_sheet.csv',index=False,index_label=False)

# acquire the unblanced panel which need be delt with
ub_panel2_sheet=ub_panel_sheet[-ub_panel_sheet.id.isin(ub_length_year.index[ub_length_year==ub_gap_year])]
ub_panel2_sheet.to_csv('ub_panel2_sheet.csv',index=False,index_label=False)
del ub_panel_sheet
del ub_panel1_sheet
del ub_panel2_sheet