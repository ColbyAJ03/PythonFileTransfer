#   File Transfer Program
#   
#   By Alex Colby
#
#   For the Tech Academy
#
#   NOTE: You must have a "Folder A" and a "Folder B" on your
#   desktop for this program to work correctly

import shutil
import glob
import os.path as path
import datetime as dt
from datetime import datetime, timedelta



srcFolder = "/Users/Alex/Desktop/Folder A/*"
dstFolder = "/Users/Alex/Desktop/Folder B/"

def fileTransfer(srcFolder,dstFolder):
    lastPass = dt.datetime.now()
    past = lastPass - dt.timedelta(hours=24)
    
    for file in glob.glob(srcFolder):
        mTime = datetime.fromtimestamp(path.getmtime(file))
        if mTime > past:
            shutil.copy(file,dstFolder)
    


