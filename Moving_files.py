# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:25:58 2022

@author: Administrator
"""

from ftplib_event_reader import cat_3
from variables import myYear, path1, cat_in_word,category,types, categories
import shutil
import os
import pandas as pd
from os.path import exists

slash = "/"
path = path1+myYear+slash+cat_in_word+"_Data"
if exists(path1 + myYear) == False:
    os.mkdir(path1 + myYear) 

def find(name, path):#return root dir and name of a given file
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def move_files():#make directory and move required files in this directory
    
    list_1 = filter_by_time()
    if exists(path) == False:
        os.mkdir(path)

    for x in range (len(list_1)):     
        src = find(list_1[4][x], 'E:\\')#Source Path
        dst = path +'/'+list_1[4][x]# Destination path
        shutil.copy(src, dst)
        continue
        return False

def filter_by_time():
    d = pd.read_csv("E:/CALLISTO/All_files_list.csv", index_col= 0).rename(columns=int)
    d.index = pd.to_datetime(d.index)
    cat = cat_3(category).index
    d.index.isin(cat)
    file = d[d.index.isin(cat)]
       
    return file

def filter_by_time(categories):
    d = pd.read_csv("E:/CALLISTO/All_files_list.csv", index_col= 0).rename(columns=int)
    d.index = pd.to_datetime(d.index)
    cat = cat_3(categories).index
    d.index.isin(cat)
    file = d[d.index.isin(cat)]
       
    return file

              




# fit_files()
# filter_by_time()
# move_files()

