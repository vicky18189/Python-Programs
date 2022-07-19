import sys
import os
import ftplib
import ftputil
import fnmatch
import time
from time import mktime
import datetime
import os.path, time 
from ftplib import FTP, ftpcp


FTP_HOST = 'ftp.universalbackground.com'
FTP_USER = 'exxat'
FTP_PASS = '*******'
dir_dest = '/' # Directory where the files needs to be downloaded to
rem_dir = '/' # Directory where the files are present on the FTP server
pattern = '*background*.pdf' #filename pattern for what the script is looking for 
print ('Looking for this pattern :', pattern) # print pattern
utc_datetime_less24H = datetime.datetime.utcnow()-datetime.timedelta(seconds=86400) #UTC time minus 24 hours in seconds
print ('UTC time less than 24 Hours is: ', utc_datetime_less24H.strftime("%Y-%m-%d %H:%M:%S")) # print UTC time minus 24 hours in seconds
print ("logging into GSP FTP") # print 
    

with ftputil.FTPHost(FTP_HOST, FTP_USER, FTP_PASS) as host: # ftp host info
    # ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    print ("logged in") # print logged in
    # ftp.encoding="utf-8"
    # ftp.dir()
    recursive = host.walk(rem_dir,topdown=True,onerror=None) # recursive search 
    for root,dirs,files in recursive:
        for name in files:
            print ('Files   :', files) # print all files it finds
            video_list = fnmatch.filter(files, pattern) # collect all files that match pattern into variable:video_list
            statinfo = host.stat(root, video_list) # get the stats from files in variable:video_list
            file_mtime = datetime.datetime.utcfromtimestamp(statinfo.st_mtime) 
            print ('Files with pattern: %s and epoch mtime is: %s ' % (video_list, statinfo.st_mtime))
            print ('Last Modified: %s' % datetime.datetime.utcfromtimestamp(statinfo.st_mtime) )
            if file_mtime >= utc_datetime_less24H: 
                for fname in video_list:
                    fpath = host.path.join(root, fname)
                    if host.path.isfile(fpath):
                        host.download_if_newer(fpath, os.path.join(dir_dest, fname), 'b') 

host.close()
