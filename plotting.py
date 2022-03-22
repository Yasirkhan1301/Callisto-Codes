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

# simple_in_tree()

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

# bg_sub_tree()



def slice_time(file_name, begin, end, freq1,freq2):
    dirs = find_Data()
    
    fit2_path = path +slash+ file_name +".fit"
    path2 = path1+ slash+ myYear +slash+ 'plots_for_'+ file_name
    path3 = path2+slash+file_name
    if exists(path2) == False:
        os.mkdir(path2)
        
        #join time axis
    joined1 = pyc.PyCallisto.from_file(fit2_path)
    plt = joined1.spectrogram() #this will show in imshow thing
    plt.savefig(path2+slash+"simple_joined.png")
    
    #slice in frequency axis
    freq_sliced = joined1.slice_frequency_axis(freq1, freq2)
    plt = freq_sliced.spectrogram() #this will show in imshow thing
    plt.savefig(path2+slash+"freq_sliced.png")
    
    
    #slice in time axis
    time_sliced = freq_sliced.slice_time_axis(begin, end)
    plt = time_sliced.spectrogram() #this will show in imshow thing
    plt.savefig(path2+slash+"time_sliced.png")
    
    
    #do background subtraction
    background_subtracted = time_sliced.subtract_background()
    plt = background_subtracted.spectrogram()
    plt.savefig(path2+slash+"bg_sub.png")
    
    return 0


# slice_time(path+ "/SONPK_20210830_120000_57.fit")
#            File Name                time range for slicing   frequency range for slicing
# slice_time("MUPK_20170905_071500_59", "07:21:00", "07:23:00","45","500")









#old version
# def simple(path):
#     fit = find(path)
#     if exists(path2) == False:
#         os.mkdir(path2)    
        
#     for x in range(len(fit)):    
#         fit_path = path+slash+fit[0][x]
#         print(x,fit[0][x])
#         #plot multiple files
#         fits1 = pyc.PyCallisto.from_file(fit_path)
#         plt = fits1.spectrogram() #this will show in imshow thing
#         plt.savefig(path2+slash+fit[1][x]+".png")
#         continue
#     return False
    
# simple(path)# To run this remove fits files that are below 100KBs


# def bg_sub(path):
    
   
#      fit = find(path)
#      if exists(path2+"_bg_sub") == False:
#          os.mkdir(path2+"_bg_sub")
         
#      for x in range(len(fit)):
#          fit_path = path+slash+fit[0][x]
#          print(x,fit[0][x])
#          fits1 = pyc.PyCallisto.from_file(fit_path)
#          background_subtracted = fits1.subtract_background()
#          plt = background_subtracted.spectrogram()
#          plt.savefig(path2+"_bg_sub"+slash+ fit[1][x]+"_bg_sub.png")
#          continue
#      return False
    
# bg_sub(path)










    
# len(files[2])

# files_os[0][0]
# fit = pd.DataFrame(file_names.filter_by_time())
# fit = fit.sort_index()
# fit.drop(labels = , axis = 0, inplace = True)


# for x in range (len(fit)-1):
    
#     fit_path = "Data/"+fit[4][x]
#     print(x,fit[4][x])
#     #plot multiple files
#     fits1 = pyc.PyCallisto.from_file(fit_path)
#     # plt = fits1.spectrogram() #this will show in imshow thing
#     # plt.savefig("Plot/"+fit[5][x]+".png")
    
    # do background subtraction
    # background_subtracted = fits1.subtract_background()
    # plt = background_subtracted.spectrogram()
    # plt.savefig("Plots_bg_sub/"+fit[5][x]+"_bg_sub.png")
    # continue
    

# #plot multiple files
# fits2 = pyc.PyCallisto.from_file(fits2_path)
# plt = fits2.spectrogram() #this will show in imshow thing
# plt.savefig("fits2.png")


# #join time axis
# joined1 = fits1.append_time_axis(fits2_path)
# plt = joined1.spectrogram() #this will show in imshow thing
# plt.savefig("joined.png")

# #slice in frequency axis
# freq_sliced = joined1.slice_frequency_axis("200", "400")
# plt = freq_sliced.spectrogram() #this will show in imshow thing
# plt.savefig("freq_sliced.png")

#MUPK_20210909_031044_59

# fits1 = pyc.PyCallisto.from_file("Data/MUPK_20210909_031044_59.fit")
# background_subtracted = fits1.subtract_background()
# plt = background_subtracted.spectrogram()
# #slice in time axis
# time_sliced = freq_sliced.slice_time_axis("03:21:00", "03:23:00")
# plt = time_sliced.spectrogram() #this will show in imshow thing
# plt.savefig("time_sliced.png")





# # #get meanlightcurve
# background_subtracted.mean_light_curve(out_image="mean_Light_Curve.png", grid=True)

# # #get meanSpectrum
# background_subtracted.mean_spectrum(out_image="mean_spectrum.png", grid=True)

# # #get light curve at one frequency
# background_subtracted.light_curve(300, out_image="Lightcurve.png", grid=True)


# # #get spectrum
# background_subtracted.spectrum( '2021/01/27','04:15:00', out_image="singletimespectrum.png", grid=True)







# # fit_path = find('GAURI_20151104_034500_59.fit', 'E:\\')
# fit_path    
# image = CallistoSpectrogram.read(fit_path)
# image.peek()

# more = image.extend()
# more.peek()

# nobg = image.subtract_bg()
# nobg.peek(vmin=0)


# bg = image.auto_const_bg()
# plt.plot(image.freq_axis, bg)
# plt.xlabel("Frequency [MHz]")
# plt.ylabel("Intensity")
# plt.show()
