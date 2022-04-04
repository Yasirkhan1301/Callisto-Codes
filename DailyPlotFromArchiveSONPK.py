# -*- coding: utf-8 -*-
"""
Created on Tue Sep 07 09:48:41 2016
Lecture 8.1/9
@author: cmonstei
"""

import sys
import matplotlib.pyplot as plt 
from astropy.io import fits
import numpy as np
import glob
from variables import date, myYear,path2,path1

slash = "/"
file_names = []

def main(path,date,ID,FC):
    
    fig, axs = plt.subplots(4, 16, figsize=(21,8), sharex=True, sharey=True)
  
    axs = axs.flatten() #from grid to flat list
    FCe = '_'+FC+'.fit'
    i = 0
    myfilter= path+ID+'_'+date[0:4]+date[5:7]+date[8:10]+'*'+FCe+'*'
    liste = glob.glob(myfilter)
    liste.sort()
    print(len(liste))
    # print (liste[65])
    for ffile in liste:
        # print (ffile)
        file_names.append(ffile)
        if FCe in ffile:
            
            hdu = fits.open(ffile)
            S = hdu[0].data
            n  = 30*4 # position in time for background analysis
            dn = 7 # number of spectra to average
            spec = S[:,n:n+dn] # take a slice of a clean part
            size = spec.shape
            columns = size[0]
            
            background = np.mean(spec,axis=1).reshape(columns,1)
            data = S - background
            data = data.clip(-1,50) # 30 adjust color-map (0dB = blue)
            freq = hdu[1].data[0][1] # frequency axis
            date = hdu[0].header['DATE-OBS']
            Thour = int(hdu[0].header['TIME-OBS'].split(":")[0])
            Tmin  = int(hdu[0].header['TIME-OBS'].split(":")[1])
            p = int(int(Thour*60+Tmin)/15 + 0.5)
            extent = (0,1, freq[-1], freq[0])
            axs[p].imshow(data, aspect="auto", extent=extent)
            axs[p].set_xticks([])                #axs[p].axis('off')
            i=i+1
            hdu.close()

    txt = '00            15             30             45              '
    xaxistxt = txt + txt + txt + txt + txt 
    fig.text(0.12, 0.07, xaxistxt, ha='left',fontsize=10.5)
    fig.text(0.055, 0.5, 'Frequency [MHz]', va='center', rotation='vertical', fontsize=15)
    fig.text(0.91, 0.84, '00-03UT', va='center', rotation='horizontal', fontsize=15)
    fig.text(0.91, 0.71, '04-07UT', va='center', rotation='horizontal', fontsize=15)
    fig.text(0.91, 0.58, '08-11UT', va='center', rotation='horizontal', fontsize=15)
    fig.text(0.91, 0.45, '12-15UT', va='center', rotation='horizontal', fontsize=15)
    fig.text(0.91, 0.32, '16-19UT', va='center', rotation='horizontal', fontsize=15)
    fig.text(0.91, 0.19, '20-23UT', va='center', rotation='horizontal', fontsize=15)
    fig.subplots_adjust(wspace=0.001, hspace=0.1)
    plt.suptitle("Full day spectra "+date+" station: "+ID+' with focus-code: '+FCe[1:3], size=16)
    plt.savefig(path1 + "Daily_Overview"+slash+myYear+slash+ ID+'_'+date[0:4]+date[5:7]+date[8:10]+'_'+FCe[1:3]+'.png')

try:
    main(path2,date,'SONPK','59') # date-code, instrument-code, focus-code

except:
    print ("Error, most probably one or more corrupt FIT-file(s): ",sys.exc_info())
