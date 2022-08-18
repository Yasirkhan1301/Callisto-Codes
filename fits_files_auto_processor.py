# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 15:03:53 2022

@author: Administrator
"""
# Event list : ftp://ftp.swpc.noaa.gov/pub/warehouse/
import shutil
import os
import pandas as pd
from os.path import exists
import glob
from sys import stdout
from time import sleep

class variables:
    def __init__(self, **kwargs):
        
        self.s = "/"
        self.types = ["I","II","III","IV","V","VI"]
        self.categories = ["1","2","3"]
        self.year = kwargs["year"]
        self.month = kwargs["month"]
        self.day = kwargs["day"]
        # self.date = self.year+"-"+self.month+"-"+self.day
        self.dst = kwargs["dst"]
        self.src = kwargs["src"]
        # self.path2 = self.path + "Daily_Overview"+self.s+self.year+self.s+self.day+self.s       

class Read_events:
    
    def __init__(self, d):
        self.path = d.dst
        self.year = str(d.year)
        self.year_int = d.year
        self.path2 = self.path+"Event list/" + self.year+"_events/*.txt"
        self.types = d.types
        self.categories = d.categories
        self.s = d.s
        self.path1 = d.dst
        self.month = d.month
        self.day = d.day
        self.source  = d.src
    def extract_files(self): # only to extract .tar.gz file, it can be done with winrar or any other software manualy 
        # archive = self.year + '_events.tar.gz'
        # tar = tarfile.open(archive, "r:gz")# download and put archive 
        # # file in the working directory   
        # for member in tar.getmembers():
        #     #print "Extracting %s" % member.name
        #     tar.extract(member, path='')  
        return False
    
    def find(self,name, path):#return root dir and name of a given file
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
            
    def fit_files_list(self):#this function save a list of all '.fit' files present in a given directory, in this case E drive.
    
        fs = []
        actual = []
        fd = []
        for root, dirs, files in os.walk(self.source): # change drive name 
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
        d[5] = pd.to_datetime(d[1]).dt.date
        d[1] = pd.to_datetime(d[1] + d[2])
        d = d.set_index(d[1])
        d.drop_duplicates(subset=[4],inplace = True)
        d.index = d.index.floor('60min')
        d.drop(labels = [1],inplace = True, axis = 1)
        d.drop(d.index[d[3].str.contains(" ")], inplace = True)
        # d.to_csv("E:/CALLISTO/All_files_list.csv" , index = True)
        return d
    
    def read_files(self):# read extracted files, combine them in a dataframe
        liste = glob.glob(self.path2)
        df1 = []
        for x in range (len(liste)-1):
            #           Event   Begind    Max       End     Obs      
            colspecs = [(0, 6),(10, 16), (18, 22),(27,32),(34,37),
                        (38,40),(40,46),(48,52),(56,63),(65,73)]
            #               Q     Type   Loc     Cat/type
            df = pd.read_fwf(liste[x], colspecs=colspecs, header = None)
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

    def search(self,index, category):#search index in parameters is for the end and begin timing column
        dfs = self.read_files()
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

    def category(self,category):#return dataframe of category passed in the parameter
        final_df = pd.concat([self.search(1,category),self.search(3,category)])
        final_df.drop(labels = [11], axis = 1, inplace = True)
        final_df.drop_duplicates(inplace = True)
        final_df
        return final_df
    
    def filter_by_time(self,g,category):# return the list of files present in the noaa solar events 
        d = g
        d.index = pd.to_datetime(d.index)
        cat = self.category(category).index
        # d.index.isin(cat)# index number
        file = d[d.index.isin(cat)]    
        return file
                  
    def categorize(self):#access types and categories, and move files in directory tree pattern
        g = self.fit_files_list()
        counter = 0
        for t in self.types:
            for c in self.categories:
                list_1 = self.filter_by_time(g,t+self.s+c)
                length = len(list_1)
                path = self.path1+self.s+self.year+self.s+t+self.s+c+self.s+"Data"
                if exists(path) == False and length:
                    os.makedirs(path)
                for x in range (len(list_1)):     
                    src = self.find(list_1[4][x], self.source)#Source Path
                    dst = path +'/'+list_1[4][x]# Destination path
                    shutil.copy(src, dst)
                    counter +=1
                    stdout.write("\r%d Files copied " % counter)
                    stdout.flush()
                    sleep(0.01)
                    continue
                    return 0
   
class copy_files:
    
    def __init__(self, d):
        self.s = d.s
        self.year = d.year
        self.month = d.month
        self.day = d.day
        self.path = d.dst
        self.fit_files_list = Read_events(d).fit_files_list
        self.find = Read_events(d).find
        self.source = d.src
  
    def copy(self, li,path):
        counter = 0
        path2 = path
        if exists(path2) == False:
            os.makedirs(path2)   
        for x in range (len(li)):     
            src = self.find(li[4][x], self.source)#Source Path
            dst = path2 +'/'+li[4][x]# Destination path
            shutil.copy(src, dst)
            counter +=1
            stdout.write("\r%d Files copied " % counter)
            stdout.flush()
            sleep(0.01)
            continue   

    def yearly(self):
        path2 = self.path+str(self.year)+self.s+"All Files"
        li = self.fit_files_list()
        li = li[li.index.year == self.year]
        self.copy(li,path2)        

    def monthly(self):
        path2 = self.path+self.year+self.s+str(self.month)+ self.s+"Data"
        li = self.fit_files_list()
        li = li[li.index.year == self.year]
        li = li[li.index.month == self.month]
        self.copy(li, path2)

    def specified_date(self):
        path2 = self.path+str(self.year)+self.s+str(self.month)+ self.s+str(self.day)+self.s+"Data"
        li = self.fit_files_list()
        li = li[li.index.year == self.year]
        li = li[li.index.month == self.month]
        li = li[li.index.day == self.day]
        self.copy(li, path2)
        
    def date_range(self): 
        per = pd.date_range(start ='1-1-2022', end ='06-01-2022', freq ='D')
        df = pd.DataFrame()
        df[1] = per.date
        df = df.set_index(df[1])
        li = self.fit_files_list()
        xf = li[li[5].isin(df.index)]
        return xf

args = {
        "year" : 2022,
        "month" : 1,
        "day" : 1,
        "src" : "E:\\",
        "dst" : "E:/CALLISTO/"        
}
# p = variables(2022,1,1,"E:\\", "E:/CALLISTO/")
p = variables(**args)
copy = copy_files(p)
c = copy.date_range()


#Calculate the number of files present in the PC and show the missing data

# class Missing:
#     def __inti__(self,year):
        
        
        
        
        
    
# read_events = Read_events(p)
# read_events.categorize()
 













# class plotting:
#     def __init__(self,d):
        
        
        
#     def find(self,path):
#     file_list = []
#     for files in os.walk(path): 
#         continue
#     files = files[2]
#     for file in files:
#         file_size = os.path.getsize(path +"\\"+file)
#         file_size = file_size/1000
#         if file_size >= 200:
#             file_list.append(file)
#         # files = find(path)
#     fit = pd.DataFrame(file_list)
#     fit[1] = fit[0].str.replace(".fit", "")
#     return fit

#     def find_Data(self):      
#         x = []
#         start = path1+slash+myYear
#         for dirpath, dirnames, filenames in os.walk(start):
#             for dirname in dirnames:
#                 if dirname == "Data":              
#                     x.append(dirpath)
#         return x
    
    
#     def simple_in_tree(self):
#         dirs = find_Data()
#         dirs = pd.Series(dirs)
        
#         for path in dirs:
#             path2 = path
#             path = path + "/Data"
#             fit = find(path) 
#             #saving plots in this dir
#             path3 = path2 + "\Plots"
#             if exists(path3) == False:            
#                 os.mkdir(path3)    
#                 fit = find(path)
#                 if exists(path2) == False:
#                     os.mkdir(path2)                    
#                 for x in range(len(fit)):    
#                     fit_path = path+slash+fit[0][x]
#                     print(x,fit[0][x])
#                     #plot multiple files
#                     fits1 = pyc.PyCallisto.from_file(fit_path)
#                     plt = fits1.spectrogram() #this will show in imshow thing
#                     plt.savefig(path3+slash+fit[1][x]+".png")
#                     continue
#                     return False
    
#     # simple_in_tree()#uncomment this to make simple specrtrogram
    
#     def bg_sub_tree(self):
        
#         dirs = find_Data()
#         dirs = pd.Series(dirs)
#         for path in dirs:
#             path2 = path
#             path = path + "/Data"
#             fit = find(path) 
#             #saving plots in this dir
#             path3 = path2 + "\Plots_bg_sub"   
#             if exists(path3) == False:  
#                 os.mkdir(path3)
#             for x in range(len(fit)):
#                   fit_path = path+slash+fit[0][x]
#                   print(x,fit[0][x])
#                   fits1 = pyc.PyCallisto.from_file(fit_path)
#                   background_subtracted = fits1.subtract_background()
#                   plt = background_subtracted.spectrogram()
#                   plt.savefig(path3+slash+ fit[1][x]+"_bg_sub.png")
#                   continue
#             continue
#             return False
    
#     # bg_sub_tree()#uncomment this to make bg subtracted spectrogram
    
#     def slice_time(self,types, category,file_name, begin, end, freq1,freq2):
        
#         # dirs = find_Data()    
#         fit_path = path1+myYear+slash+types+slash+category+slash+"Data"+slash+file_name+".fit"
#         path2 = path1+myYear+slash+ 'plots_for_'+types+"_"+category+"_"+file_name
#         if exists(path2) == False:
#             os.mkdir(path2)
            
#             #join time axis
#         joined1 = pyc.PyCallisto.from_file(fit_path)
#         plt = joined1.spectrogram() #this will show in imshow thing
#         plt.savefig(path2+slash+"simple_joined.png")
        
#         # slice in frequency axis
#         freq_sliced = joined1.slice_frequency_axis(freq1, freq2)
#         plt = freq_sliced.spectrogram() #this will show in imshow thing
#         plt.savefig(path2+slash+"freq_sliced.png")
        
#         #do background subtraction
#         background_subtracted = freq_sliced.subtract_background()
#         plt = background_subtracted.spectrogram()
#         plt.savefig(path2+slash+"bg_sub.png")
    
        
#         #slice in time axis
#         time_sliced = freq_sliced.slice_time_axis(begin, end)
#         # time_sliced = freq_sliced.slice_time_axis(begin, end)
#         plt = time_sliced.spectrogram() #this will show in imshow thing
#         plt.savefig(path2+slash+"time_sliced.png")
        
        
#         #do background subtraction
#         background_subtracted = time_sliced.subtract_background()
#         plt = background_subtracted.spectrogram()
#         plt.savefig(path2+slash+"time_sliced_bg_sub.png")
        
#         return 0
        
        
        