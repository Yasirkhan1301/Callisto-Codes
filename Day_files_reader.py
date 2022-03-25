# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 14:55:38 2022

@author: Administrator
"""
import os
import datetime
# traverse whole directory
import pandas as pd
from variables import date, myYear,path1
from os.path import exists
import shutil

slash = "/"
def fit_files():
    
        fs = []
        actual = []
        fd = []

        for root, dirs, files in os.walk(r'E:\\CALLISTO\\Data'):
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
        # d.index = d.index.floor('60min')
        d.drop(labels = [1],inplace = True, axis = 1)
        d.drop(d.index[d[3].str.contains(" ")], inplace = True)
        # d.to_csv("E:/CALLISTO/All_files_list.csv" , index = True)
        return d
    
def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
        
def move_files():
    d = pd.DataFrame(fit_files())
    list_1 = d.loc[date]
    path2 = path1 + "Daily_Overview"+slash+myYear+slash+date 
    path2
    if exists(path2) == False:
        os.makedirs(path2+slash)

    for x in range (len(list_1)):     
        src = find(list_1[4][x],path1+slash+"Data")#Source Path
        dst = path2+slash+list_1[4][x]# Destination path
        shutil.copy(src, dst)
        continue
        return False

move_files()
