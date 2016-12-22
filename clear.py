import os

extension = '.dmp'
directory = 'C:\Samsara2\'

filelist = [ f for f in os.listdir(".") if f.endswith(extension) ]
for f in filelist:
    os.remove(f)

