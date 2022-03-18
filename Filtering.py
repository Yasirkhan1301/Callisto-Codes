# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 15:09:36 2022

@author: Administrator
"""

import os
import datetime
# traverse whole directory
import pandas as pd


def fit_files():
    
        fs = []
        actual = []
        fd = []

        for root, dirs, files in os.walk(r'E:\\'):
            # select file name
            for file in files:
                # check the extension of files
                if file.endswith('.fit'):
                    # print whole path of files             
                    fs.append(file.split('_'))
                    fd.append(file)
                    actual.append(file.split('.'))
 
        d = pd.DataFrame(fs)
        ds = pd.DataFrame(actual)
        d[3],d[4] = ds[0] , fd
        d.drop(d.index[d[1].isnull()], inplace = True)
        d[1] = pd.to_datetime(d[1] + d[2])
        d = d.set_index(d[1])
        d.drop_duplicates(subset=[4],inplace = True)
        d.index = d.index.floor('60min')
        d.drop(labels = [1],inplace = True, axis = 1)
        d.drop(d.index[d[3].str.contains(" ")], inplace = True)
        d.to_csv("E:/CALLISTO/All_files_list.csv" , index = True)
        return d
    

fit_files()









# def filter_by_time():
#     d = fit_files()
#     cat = cat_3(category).index
#     d.index.isin(cat)
#     file = d[d.index.isin(cat)]
#     return file
    
    

    




















 # d[2] = pd.to_datetime(d[2])
 #        d.set_index(d[1] + d[2])
 #        d.index = pd.to_datetime(d.index)
 #        d
 #        d[4] = actual
 #        d.drop_duplicates(subset = [] , inplace = True)
 #        d[3] = d[1]
 #        d[1] = d[1] + d[2]
 #        d[[1]] = d[[1]].apply(pd.to_datetime)
 #        d = d.set_index([1])
 #        d.drop(
 #                d.index[d[0] == "GAURI"] | d.index[d[0] == "IISERP"],
 #                inplace = True
 #                )
        
 #        fin = []
 #        n = event_dates.events().index
 #        d.index = d.index.floor('60min')
 #        dfa = d[d.index.isin(n)]
 #        df = pd.DataFrame(dfa[4])