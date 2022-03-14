# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 15:17:04 2018
Old event lists for download here: ftp://ftp.swpc.noaa.gov/pub/warehouse/
Lecture 4.6/5 read NOAA-server and make list of type II bursts
@author: Christian Monstein
"""
#-----------------------------------------------------------------------

import urllib3
import tarfile
import glob

#-----------------------------------------------------------------------
myYear = '2021'
BurstType = 6 # 1....6

archive = myYear + '_events.tar.gz'
bursttypes = [' I/',' II/',' III/',' IV/',' V/',' CTM']
burstnames = ['TypeI','TypeII','TypeIII','TypeIV','TypeV','TypeCTM']
# CTM = Broadband, long-lived, dekametric continuum
# If yu have internet access switch off comments lines 23-29

"""
url = 'ftp://ftp.swpc.noaa.gov/pub/warehouse/' + myYear + '/'
myurl = url + archive
print ("Downloading Event-file with urllib from: " + myurl)
#urllib.urlcleanup()
urllib.request.urlretrieve(myurl, archive)

tar = tarfile.open(archive, "r:gz")
#print tar.getnames()
for member in tar.getmembers():
    #print "Extracting %s" % member.name
    tar.extract(member, path='')
"""
liste = glob.glob(myYear+"_events/*.txt")
liste.sort()

outF = open("MyBurstFile_" + burstnames[BurstType-1] + "_" + myYear + ".txt", "w")
title = ' #Event    Begin    Max       End  Obs  Q  Type  Loc/Frq   Particulars       Reg#'
print (liste[0],title)
outF.write(liste[0] + ' '  + title)
outF.write('\n')

for day in liste:
    f = open(day, 'r')
    for line in f:
        if bursttypes[BurstType-1] not in (line): 
            continue 
        text = day + '->' + line
        print (text, end=" ")
        outF.write(text)
    f.close()
outF.close()