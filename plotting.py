# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 10:33:12 2022

@author: Administrator
"""
#For Plotting the data
import os
import sys
import pyCallisto as pyc
import pyCallisto_Utils as utils
#import pyfits
import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from variables import path1, myYear
from os.path import exists
from matplotlib import cm

slash = "/"

def find(path):
    file_list = []
    for files in os.walk(path): 
        continue
    files = files[2]
    for file in files:
        file_size = os.path.getsize(path +"\\"+file)
        file_size = file_size/1000
        if file_size >= 200:
            file_list.append(file)
        # files = find(path)
    fit = pd.DataFrame(file_list)
    fit[1] = fit[0].str.replace(".fit", "")
    return fit

 
def find_Data():      
    x = []
    start = path1+slash+myYear
    for dirpath, dirnames, filenames in os.walk(start):
        for dirname in dirnames:
            if dirname == "Data":              
                x.append(dirpath)
    return x


def simple_in_tree():
    dirs = find_Data()
    dirs = pd.Series(dirs)
    
    for path in dirs:
        path2 = path
        path = path + "/Data"
        fit = find(path) 
        #saving plots in this dir
        path3 = path2 + "\Plots"
        if exists(path3) == False:            
            os.mkdir(path3)    
            fit = find(path)
            if exists(path2) == False:
                os.mkdir(path2)                    
            for x in range(len(fit)):    
                fit_path = path+slash+fit[0][x]
                print(x,fit[0][x])
                #plot multiple files
                fits1 = pyc.PyCallisto.from_file(fit_path)
                plt = fits1.spectrogram() #this will show in imshow thing
                plt.savefig(path3+slash+fit[1][x]+".png")
                continue
                return False

simple_in_tree()

def bg_sub_tree():
    
    dirs = find_Data()
    dirs = pd.Series(dirs)
    for path in dirs:
        path2 = path
        path = path + "/Data"
        fit = find(path) 
        #saving plots in this dir
        path3 = path2 + "\Plots_bg_sub"   
        if exists(path3) == False:  
            os.mkdir(path3)
        for x in range(len(fit)):
              fit_path = path+slash+fit[0][x]
              print(x,fit[0][x])
              fits1 = pyc.PyCallisto.from_file(fit_path)
              background_subtracted = fits1.subtract_background()
              plt = background_subtracted.spectrogram()
              plt.savefig(path3+slash+ fit[1][x]+"_bg_sub.png")
              continue
        continue
        return False

bg_sub_tree()


def slice_time( fit2_path,file_name, begin, end, freq1,freq2):
    
    # dirs = find_Data()    
    fit_path = fit2_path +slash+"Data"+slash+file_name+".fit"
    path2 = fit2_path +slash+ 'plots_for_'+ file_name
    path3 = path2+slash+file_name
    if exists(path2) == False:
        os.mkdir(path2)
        
        #join time axis
    joined1 = pyc.PyCallisto.from_file(fit_path)
    plt = joined1.spectrogram() #this will show in imshow thing
    plt.savefig(path2+slash+"simple_joined.png")
    
    # slice in frequency axis
    freq_sliced = joined1.slice_frequency_axis(freq1, freq2)
    plt = freq_sliced.spectrogram() #this will show in imshow thing
    plt.savefig(path2+slash+"freq_sliced.png")
    
    
    #slice in time axis
    time_sliced = freq_sliced.slice_time_axis(begin, end)
    # time_sliced = freq_sliced.slice_time_axis(begin, end)
    plt = time_sliced.spectrogram() #this will show in imshow thing
    plt.savefig(path2+slash+"time_sliced.png")
    
    
    #do background subtraction
    background_subtracted = time_sliced.subtract_background()
    plt = background_subtracted.spectrogram()
    plt.savefig(path2+slash+"bg_sub.png")
    
    return 0

# types = "III"
# category= "2"
# file_name = "MUPK_20210524_103000_59"
# data_path = path1+myYear+slash+types+slash+category
# # slice_time(path+ "/SONPK_20210830_120000_57.fit")
# #            File Name,                time range for slicing,   frequency range for slicing , data path
# slice_time(data_path, file_name, "10:36:00", "10:38:00","45","850")

