# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:29:27 2022

@author: Administrator

Event list : ftp://ftp.swpc.noaa.gov/pub/warehouse/

"""
import tarfile
import glob
import pandas as pd
# from ftplib import FTP
from variables import myYear, path1

path = path1

def extract_files(): # only to extract .tar.gz file, it can be done with winrar or any other software manualy
    
    archive = myYear + '_events.tar.gz'
    
    
    tar = tarfile.open(archive, "r:gz")# download and put archive 
    # file in the working directory
    
    for member in tar.getmembers():
        #print "Extracting %s" % member.name
        tar.extract(member, path='')
        
    return False
    

# extract_files()

def read_files():# read extracted files, combine them in a dataframe
    liste = glob.glob(path + myYear+"_events/*.txt")
    df1 = []
    
    for x in range (len(liste)-1):
        
        #           Event   Begind    Max       End     Obs      
        colspecs = [(0, 6),(10, 16), (18, 22),(27,32),(34,37),
                    (38,40),(40,46),(48,52),(56,63),(65,73)]
        #               Q     Type   Loc     Cat/type
        
        df = pd.read_fwf(liste[x], colspecs=colspecs, header = None)
        df
        
        df.drop(
                labels = [0,1,2,3,4,5,6,7,8,9,10,11],
                axis = 0,
                inplace = True)
        df.drop(
            df.index[df[1].isnull()],
            inplace = True)
        xf = liste[x].split("\\")
        xf = xf[1].split(".")
        xf = xf[0].replace("events","")
        df[10] = xf
        df
        df1.append(df)
        continue
    return df1


def cat_3_3(index, category):#index in parameters is for the end and begin timing column
    dfs = read_files()
    final = pd.concat(dfs)
    final.drop(
            final.index[final[index].isnull()],
            inplace = True)
    final.drop(
        final.index[final[index].str.contains("[a-zA-Z]")],#for removing alphabets
        inplace = True
        )
    final[11] = final[10] + final[index]
    final[11] = pd.to_datetime(final[11])
    cat_3 = final[final[8] == category]
    cat_3 = cat_3.set_index(cat_3[11])
    cat_3 =  cat_3.between_time('00:30', '15:00')
    cat_3.index = cat_3.index.floor('60min')
    
    return cat_3
    

def cat_3(category):#return dataframe of category passed in the parameter
    final_df = pd.concat([cat_3_3(1,category),cat_3_3(3,category)])
    final_df.drop(labels = [11], axis = 1, inplace = True)
    final_df.drop_duplicates(inplace = True)
    final_df
    return final_df

#uncomment following lines for testing

# cat_3_3(3,"III/2")
# cat_3_3(3, "III/3")[11]

