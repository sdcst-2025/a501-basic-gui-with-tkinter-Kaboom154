'''
##### Task 1
Create the user interface described in the image task1.png.
You should use only the .pack() or .grid() methods
(2 points) 
'''

import tkinter as tk
from tkinter import *

# future improvements: make '=' button work with 'ENTER' key

window = tk.Tk()
window.geometry('400x30')
window.attributes("-topmost",True)


def multiplyButton():
    num1 = int(entry1.get())
    num2 = int(entry2.get())
    value = num1 * num2
    lable2.config(text=value)

#def entryCheck(text):       # old function with validation
#    try:
#        text = int(text)
#    except:
#        return False
#    return True

entry1 = tk.Entry(window, width=15, textvariable=IntVar()) #, validate='key',validatecommand=(window.register(entryCheck),'%P')) 
entry2 = tk.Entry(window, width=15, textvariable=IntVar()) #   ^ stops any deletion or entry of non-int

lable1 = tk.Label(window, text='X')
lable2 = tk.Label(window, text=0, bg="#b4b1ce") #need lable to continually update

button1 = tk.Button(window, text='=', command=multiplyButton)


#root = Tk()
#s = Label(root, text="0")
#s.pack()
#root.after(2000, s.config(text="2"))
#root.mainloop()


entry1.grid(row=1, column=1)
lable1.grid(row=1, column=2)
entry2.grid(row=1, column=3)
button1.grid(row=1, column=4)
lable2.grid(row=1, column=6)


window.mainloop()
