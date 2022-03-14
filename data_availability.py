# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:52:27 2022

@author: Administrator
"""
import os
import pandas as pd

def data_availability():
    
    files_name = []
    actual = []
    fs = []
    
    for root, dirs, files in os.walk(r'E:\\'):
        # select file name
        for file in files:
            # check the extension of files
            if file.endswith('.fit'):
                # print whole path of files
                ds = file.split('.')
                files_name.append(ds[0].split('_'))
                actual.append(file)
                fs.append(file.split('.'))
                continue
            
    d = pd.DataFrame(files_name)
    return d


data = data_availability()
data[1] = pd.to_datetime(data[1])

data.drop(
    data.index[data[1].isnull()] ,   
    inplace = True)
data = data.set_index(data[1])
data.drop_duplicates(inplace = True)
data

years = []

for x in range(2017, 2022):
    month = []    
    av = data[data.index.year == x]    
    for y in range(1,13):
        at = av.index[av.index.month == y]
        month.append(len(at))
        continue
    years.append(month)
    continue
    
df = pd.DataFrame(years)
df.to_csv("Data_availability.csv",index = False)
   


    
   
    

