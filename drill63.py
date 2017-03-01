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

srcFolder = "/Users/Alex/Desktop/Folder A/*"
dstFolder = "/Users/Alex/Desktop/Folder B/"


for file in glob.glob(srcFolder):
    print("Moving {} to {}".format(file,dstFolder) )
    shutil.move(file,dstFolder)

