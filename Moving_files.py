# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:25:58 2022

@author: Administrator
"""

from ftplib_event_reader import cat_3
from variables import myYear, path1, cat_in_word,category
from Filtering import fit_files
import shutil
import os


path = path1+myYear+"/"+cat_in_word+"_Data"
path
# os.mkdir(path1 + myYear) # comment this when year folder already exist

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def move_files():
    
    list_1 = filter_by_time()
    # os.mkdir(path)
    for x in range (len(list_1)-1):     
        src = find(list_1[4][x], 'E:\\')#Source Path
        dst = path +'/'+list_1[4][x]# Destination path
        shutil.copy(src, dst)
        continue
        return False

def filter_by_time():
    d = fit_files()
    cat = cat_3(category).index
    d.index.isin(cat)
    file = d[d.index.isin(cat)]
    # file.drop_duplicates(subset = [4], inplace = True)
    return file

# filter_by_time()
move_files()

