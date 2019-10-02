from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import GuiMainWindowDrill
import guiDrill

def askDir(self):
    fileDir = filedialog.askdirectory()
    self.txt_browse1.delete(0, END)
    self.txt_browse1.insert(0, fileDir)

def askDir2(self):
    fileDir2 = filedialog.askdirectory()
    self.txt_browse2.delete(0, END)
    self.txt_browse2.insert(0, fileDir2)


