'''Aquire Balanced and Unbalanced Panel Data from the China's Manufacturing Database 
'''

from pandas import *
from numpy import *

# read the data
panel=read_csv('data.csv')
total_year=2007-1998+1

# exclude one-year data
length_year = (panel.groupby('id')['year'].size())
panel = panel[-panel.id.isin(length_year[length_year==1].index)]
panel.to_csv('panel.csv')
del panel

# read the panel
panel = read_csv('panel.csv')

# select the balanced panel
balanced_panel = panel[panel.id.isin(length_year[length_year==total_year].index)]
balanced_panel.to_csv('balanced_panel.csv')
del balanced_panel


# acquire the unbalanced panel which needs to deal with
ub_panel =  panel[-panel.id.isin(length_year[length_year==total_year].index)]
ub_panel.to_csv('ub_panel.csv')
del panel
del ub_panel

# read the unbalanced panel data
ub_panel = read_csv('ub_panel.csv')

# acquire the unbalanced panel which need not be delt with
ub_gap_year = ub_panel.groupby('id')['year'].apply(max)-ub_panel.groupby('id')['year'].apply(min)+1
ub_length_year = ub_panel.groupby('id')['year'].size()
ub_panel1=ub_panel[ub_panel.id.isin(ub_length_year.index[ub_length_year==ub_gap_year])]
ub_panel1.to_csv('ub_panel1.csv')
ub_panel2=ub_panel[-ub_panel.id.isin(ub_length_year.index[ub_length_year==ub_gap_year])]
ub_panel2.to_csv('ub_panel2.csv')
del ub_panel
del ub_panel1
del ub_panel2