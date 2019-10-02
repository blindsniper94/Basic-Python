from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import GuiMainWindowDrill
import guiDrill
import os
import sqlite3
import shutil



def create_db():
    conn = sqlite3.connect('txtfiles.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_files ( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT)")
        conn.commit()
    conn.close()

def askDir(self):
    fileDir = filedialog.askdirectory()
    self.txt_browse1.delete(0, END)
    self.txt_browse1.insert(0, fileDir)

def askDir2(self):
    fileDir2 = filedialog.askdirectory()
    self.txt_browse2.delete(0, END)
    self.txt_browse2.insert(0, fileDir2)


def chk4Files(self):
    conn = sqlite3.connect('txtfiles.db')
    myDir = self.txt_browse1.get()
    newDir = self.txt_browse2.get()
    modTime = os.path.getmtime(myDir)
    
    for file in os.listdir(myDir): # C:/Users/Alex/Documents/Tech Academy Notes/Python/PythonDrills
        if file.endswith(".txt"):
            filepath = os.path.join(myDir,file)
            print(os.path.join(myDir,file),modTime)
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_files( col_filename ) VALUES (?)",(file,))
                conn.commit()
            
            shutil.move(filepath,newDir)
            print(file,"Has been moved to:",newDir)
    conn.close()
        