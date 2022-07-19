import paramiko

host = "ftp.universalbackground.com"  # hard-coded
port = 22
transport = paramiko.Transport((host, port))

password = "T7B7vtG!EvTZ"  # hard-coded
username = "exxat"  # hard-coded
transport.connect(username=username, password=password)

sftp = paramiko.SFTPClient.from_transport(transport)

import sys
path = './' + sys.argv[1]  # hard-coded
localpath = sys.argv[1]
sftp.put(localpath, path)

sftp.close()
transport.close()
print ('Upload done.')
