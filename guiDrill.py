
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import GuiMainWindowDrill

def load_gui(self):

    #Textboxes
    self.txt_browse1 = tk.Entry(self.master,width = 40, text = '')
    self.txt_browse1.grid(row = 1, column = 2,columnspan = 2,padx = (10,40), sticky = W+E)
    self.txt_browse2 = tk.Entry(self.master,width = 40, text = '')
    self.txt_browse2.grid(row = 2, column = 2,columnspan = 2,padx = (10,40), sticky = W+E)
    #Buttons
    self.btn_browse1 = tk.Button(self.master, width = 12, height = 1, text = "Browse...")
    self.btn_browse1.grid(row = 1,column = 1,padx=(30,20),pady = (5,5))
    self.btn_browse2 = tk.Button(self.master, width = 12, height = 1, text = "Browse...")
    self.btn_browse2.grid(row = 2,column = 1,padx=(30,20),pady = (5,5))
    self.btn_Chk4files = tk.Button(self.master, width = 12, height = 2, text = "Check for files...")
    self.btn_Chk4files.grid(row = 3,column = 1,padx=(30,20),pady = (5,5))
    self.btn_close = tk.Button(self.master, width = 12, height = 2, text = "Close Program")
    self.btn_close.grid(row = 3,column = 2, columnspan = 2,padx=(30,40),pady = (5,5), sticky = E)
if __name__ == "__main__":
    pass