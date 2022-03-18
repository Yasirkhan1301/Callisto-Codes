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
path = path1+myYear+"/"+cat_in_word+"_Data"
if exists(path1 + myYear) == False:
    os.mkdir(path1 + myYear) 

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def move_files():
    
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

def move_files_auto():
      for x in range (len(types)):
        for j in range(len(categories)):
            list_1 = filter_by_time(types[x]+slash+categories[j])
            if len(list_1):
                path = path1 + myYear+slash+types[x]+slash+categories[j]+slash+"Data"+slash
                if exists(path) == False:
                    os.makedirs(path)         
                for c in range (len(list_1)):     
                  src = find(list_1[4][c], 'E:\\')#Source Path
                  dst = path+list_1[4][c]# Destination path
                  shutil.copy(src, dst)
                  continue
            continue
        continue
        return False
              
move_files_auto()




# fit_files()
# filter_by_time()
# move_files()










# def move_files_specific():# by using list
    
#     # list_1 = filter_by_time()
#     list_1 = pd.read_csv("E:/CALLISTO/list.txt", header = None)
#     list_1[0][1] = list_1[0][1].toString()

#     for x in range (len(list_1)-1):
#         list_1[0][x] = list_1[0][x].toString()
#         print(list_1[0][x])

#         src = find((list_1[0][x]), 'E:\\')#Source Path
#         dst = "E:/CALLISTO/Specific/"+list_1[0][x]# Destination path
#         shutil.copy(src, dst)
#         continue
#         return False

# move_files_specific()