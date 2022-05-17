# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:15:41 2022

@author: Administrator
"""

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






 # d[2] = pd.to_datetime(d[2])
 #        d.set_index(d[1] + d[2])
 #        d.index = pd.to_datetime(d.index)
 #        d
 #        d[4] = actual
 #        d.drop_duplicates(subset = [] , inplace = True)
 #        d[3] = d[1]
 #        d[1] = d[1] + d[2]
 #        d[[1]] = d[[1]].apply(pd.to_datetime)
 #        d = d.set_index([1])
 #        d.drop(
 #                d.index[d[0] == "GAURI"] | d.index[d[0] == "IISERP"],
 #                inplace = True
 #                )
        
 #        fin = []
 #        n = event_dates.events().index
 #        d.index = d.index.floor('60min')
 #        dfa = d[d.index.isin(n)]
 #        df = pd.DataFrame(dfa[4])
 
 
 


# def filter_by_time():
#     d = fit_files()
#     cat = cat_3(category).index
#     d.index.isin(cat)
#     file = d[d.index.isin(cat)]
#     return file




# def move_files_auto():
#       for x in range (len(types)):
#         for j in range(len(categories)):
#             list_1 = filter_by_time(types[x]+slash+categories[j])
#             if len(list_1):
#                 path = path1 + myYear+slash+types[x]+slash+categories[j]+slash+"Data"+slash
#                 if exists(path) == False:
#                     os.makedirs(path)         
#                 for c in range (len(list_1)):     
#                   src = find(list_1[4][c], 'E:\\')#Source Path
#                   dst = path+list_1[4][c]# Destination path
#                   shutil.copy(src, dst)
#                   continue
#             continue
#         continue
#         return False