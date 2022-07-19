from fileinput import filename
import ftplib

FTP_HOST = 'ftp.dlptest.com'
FTP_USER = 'dlpuser'
FTP_PASS = 'rNrKYTX9g7z3RgJRmxWuGHbeu'

ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
ftp.encoding="utf-8"


# To Upload a file on FTP server
filename='test.txt'
with open(filename, 'rb') as f:
    ftp.storbinary('STOR test.txt', f)
ftp.dir()

# To Download a file from FTP server
# filename = 'test.txt'
# with open(filename, 'wb') as f:
#     ftp.retrbinary('RETR test.txt', f.write)
# ftp.dir()




ftp.quit()