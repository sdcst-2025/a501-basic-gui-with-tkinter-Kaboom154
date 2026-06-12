'''
##### Task 1
Create the user interface described in the image task1.png.
You should use only the .pack() or .grid() methods
(2 points) 
'''

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.attributes("-topmost",True)

entry1 = tk.Entry(window,width=20)

entry1.pack()

window.mainloop()