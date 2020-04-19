# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:24:45 2020

@author: yun liu
"""
import pandas as pd

month = pd.read_csv("Month.csv",low_memory=False)
monthSlice=month.iloc[:,944:1181]
print(monthSlice.columns)#see the titles
#remova hash
dfr=monthSlice.loc[:,~monthSlice.columns.str.contains('_hash')] 
#remove lag excepet lag01, since otheres can get from lag01
dfr1=dfr.loc[:,~dfr.columns.str.contains('lag02|lag03|lag04|lag05|lag06')]

#remove all the columns that are all nan 
dfr2=dfr1
nn=dfr1.shape
for i in range(nn[1]):
    if dfr1.iloc[:,i].isnull().sum()==nn[0]:
        dfr2.pop(dfr1.columns[i])
#find all number of 0 in each columns
dfr2.isin([0]).sum()
#remove all the columns that only contain 0 or nan.
monthLastPart=dfr2.loc[:,~dfr2.columns.str.contains('_isprotected|_isrespite|_sequence|_string')]
#output the final data frame
monthLastPart.to_csv('LastPart.csv')