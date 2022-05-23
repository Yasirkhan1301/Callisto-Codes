# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:25:58 2022

@author: Administrator

Event list : ftp://ftp.swpc.noaa.gov/pub/warehouse/

"""
from ftplib_event_reader import cat_3
from variables import myYear, path1,types,categories
import shutil
import os
import pandas as pd
from os.path import exists


slash = "/"
path = path1+myYear

if exists(path1 + myYear) == False:
    os.mkdir(path1 + myYear) 
    
def fit_files():#this function save a list of all '.fit' files present in a given directory, in this case E drive.
    
        fs = []
        actual = []
        fd = []

        for root, dirs, files in os.walk(r'E:\\'): # change drive name 
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
    
# fit_files()# uncomment this to save or update the fits files list available in E directory(where your data resides)

def find(name, path):#return root dir and name of a given file
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def filter_by_time(categories):# return the list of files present in the noaa solar events 
    d = pd.read_csv("E:/CALLISTO/All_files_list.csv", index_col= 0).rename(columns=int)
    d.index = pd.to_datetime(d.index)
    cat = cat_3(categories).index
    d.index.isin(cat)
    file = d[d.index.isin(cat)]
       
    return file
              
def dir_tree():#access types and categories, and move files in directory tree pattern
    for t in types:
        for c in categories:
            list_1 = filter_by_time(t+slash+c)
            length = len(list_1)
            path = path1+slash+myYear+slash+t+slash+c+slash+"Data"
            if exists(path) == False and length:
               os.makedirs(path)
            for x in range (len(list_1)):     
                src = find(list_1[4][x], 'E:\\')#Source Path
                dst = path +'/'+list_1[4][x]# Destination path
                shutil.copy(src, dst)
                continue
                return 0
            
# dir_tree()  #uncomment this line to save the data according to its type and cateogry
     
            


    


