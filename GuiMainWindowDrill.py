
from tkinter import *
import tkinter as tk
from tkinter import messagebox

import guiDrill
import guiDrill_func    

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500, 125) # Width / Height
        self.master.maxsize(500, 125)
        self.master.title("Check files")

        guiDrill.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()