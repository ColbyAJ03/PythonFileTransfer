#   File Transfer GUI
#
#   By Alexander Colby
#
#   For The Tech Academy
#
#   Made in Python 3.5, tested on Windows 10 

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import shutil
import os.path as path
import datetime as dt
from datetime import datetime, timedelta

# frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define master frame configuration
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        # center app on user's screen
        center_window(self,500,300)
        self.master.title('File Transfer GUI')
        # built in method to catch if the close button is clicked
        self.master.protocol('WM_DELETE_WINDOW', lambda: ask_quit(self))
        arg = self.master

        # load in gui widgets from our other module
        load_gui(self)

def load_gui(self):  
    self.lbl_src = tk.Label(self.master,text='Source Folder:')
    self.lbl_src.grid(row=0,column=1,padx=(5,0),pady=(10,0),sticky=N+W)
    self.lbl_dest = tk.Label(self.master,text='Destination Folder:')
    self.lbl_dest.grid(row=1,column=1,padx=(5,0),pady=(10,0),sticky=N+W)

    # displays currently selected directories
    self.lbl_srcFolderText = StringVar()
    self.lbl_srcFolder = tk.Label(self.master,textvariable=self.lbl_srcFolderText)
    self.lbl_srcFolder.grid(row=0,column=2,padx=(0,0),pady=(10,0),sticky=N+W)
    self.lbl_destFolderText = StringVar()
    self.lbl_destFolder = tk.Label(self.master,textvariable=self.lbl_destFolderText)
    self.lbl_destFolder.grid(row=1,column=2,padx=(0,0),pady=(10,0),sticky=N+W)

    self.btn_getSrc = tk.Button(self.master,width=6,height=1,text='Select',command=lambda: getSource(self))
    self.btn_getSrc.grid(row=0,column=0,padx=(10,0),pady=(10,10),sticky=W)
    self.btn_getDest = tk.Button(self.master,width=6,height=1,text='Select',command=lambda: getDest(self))
    self.btn_getDest.grid(row=1,column=0,padx=(10,0),pady=(10,10),sticky=W)
    self.btn_run = tk.Button(self.master,width=12,height=2,text='Run Script',command=lambda: checkDirectories(self))
    self.btn_run.grid(row=8,column=0,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: ask_quit(self))
    self.btn_close.grid(row=8,column=1,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)
   
def getSource(self):
    self.srcFolder = askdirectory()
    self.lbl_srcFolderText.set(self.srcFolder)
    

def getDest(self):
    self.destFolder = askdirectory()
    self.lbl_destFolderText.set(self.destFolder)

# checks if a source and destination have been selected. Displays error if not.
def checkDirectories(self):
    try:
        transferFiles(self,self.srcFolder,self.destFolder)
    except AttributeError:
        messagebox.showerror("Invalid Directories", "Please select two valid directories")

# transfer files between folders
def transferFiles(self,srcFolder,destFolder):
    lastPass = dt.datetime.now()
    past = lastPass - dt.timedelta(hours=24)

    for f in os.listdir(srcFolder):
        file = os.path.realpath(os.path.join(srcFolder,f))
        mTime = datetime.fromtimestamp(path.getmtime(file))
        if mTime > past:
            print(file, "copied to: ", destFolder)
            shutil.copy(file,destFolder)
 

# functions for the GUI
def center_window(self,w,h): # pass in the tkinter frame (master) reference and the width and height
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinets to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # close the app
        self.master.destroy()
        os._exit(0)

# loop code        
if __name__ == '__main__':
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
