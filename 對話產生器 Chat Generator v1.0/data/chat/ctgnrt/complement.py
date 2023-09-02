import os
import shutil
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as tkfd
# ----- all widgets ----- #
class File():
    def __init__(self, master, heading_title, text_label, command):
        self = tk.Menu(master,tearoff=False)
        for i in range(len(text_label)):
            self.add_command(label=text_label[i],command= command[i])
        master.add_cascade(label=heading_title,menu = self)
class Mode():
    def __init__(self, master, heading_title, text_label, command, Mode, temp):
        self = tk.Menu(master,tearoff=False)
        for i in range(len(text_label)):
            self.add_radiobutton(label=text_label[i],variable=temp,command= command[i])
            if i == Mode:temp.set(text_label[i])
        master.add_cascade(label=heading_title,menu = self)

# billboard turn into int
def billboard_turn_int(x):
    if x.get() == "center(預設)": return 0
    elif x.get() == "fixed": return 1
    else: return 2
# alignment turn into int
def alignment_turn_int(x):
    if x.get() == "center(預設)": return 0
    elif x.get() == "left": return 1
    else: return 2