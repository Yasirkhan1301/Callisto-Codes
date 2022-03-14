# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:29:27 2022

@author: Administrator
"""
import tarfile
import glob
import pandas as pd
# from ftplib import FTP
from variables import myYear, path1

path = path1


def extract_files():
    
    archive = myYear + '_events.tar.gz'
    
    
    tar = tarfile.open(archive, "r:gz")# download and put archive 
    # file in the working directory
    
    for member in tar.getmembers():
        #print "Extracting %s" % member.name
        tar.extract(member, path='')
        
    return False
    

# extract_files()

def read_files():
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
    

def cat_3(category):
    final_df = pd.concat([cat_3_3(1,category),cat_3_3(3,category)])
    final_df.drop(labels = [11], axis = 1, inplace = True)
    final_df.drop_duplicates(inplace = True)
    final_df
    return final_df


# cat_3_3(3, "III/3")[11]




























# def cat_3_end():
    
#     dfs = read_files()
#     final = pd.concat(dfs)
#     final.drop(
#             final.index[final[3].isnull()],
#             inplace = True)
#     final.drop(
#         final.index[final[3].str.contains("[a-zA-Z]")],#for removing alphabets
#         inplace = True
#         )
#     final[11] = final[10] + final[3]
#     final[11] = pd.to_datetime(final[11])
#     cat_3 = final[final[8] == "III/3"]
#     cat_3 = cat_3.set_index(cat_3[11])
#     cat_3.drop(labels = [11], axis = 1, inplace = True)
#     cat_3 =  cat_3.between_time('00:30', '15:00')
#     cat_3.index = cat_3.index.floor('60min')
#     return cat_3
   





    















# for day in liste:
#     f = open(day, 'r')
    

#     for line in f:
#         if ':' not in (line):
#             if '#' not in (line):
#                 fx.append(day + '    ' + line)
#                 continue
     

        
      
        
      
        
      # burstnames[BurstType-1]
# outF = open("MyBurstFile_" + burstnames[BurstType-1] + "_" + myYear + ".txt", "w")
# title = ' #Event    Begin    Max       End  Obs  Q  Type  Loc/Frq   Particulars       Reg#'
# print (liste[0],title)
# outF.write(liste[0] + ' '  + title)
# outF.write('\n')



        # if bursttypes[BurstType-1] not in (line): 
        #     continue 
        # text = day + '->' + line
        # print (text, end=" ")
        # fx.append(text.)
        # outF.write(text)
# dfd = pd.DataFrame(fx)
# dfd
#     f.close()
# outF.close()
# dfd


# FTP_host = 'ftp.swpc.noaa.gov'

# FTP = ftplib.FTP()
# FTP.connect(FTP_host)
# FTP.login()
# FTP.cwd("/pub/warehouse/" + myYear + "/")
# FTP.retrlines("LIST")
# FTP.retrbinary(tarfile.open(archive,"r:gz"),print)

