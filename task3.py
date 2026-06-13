'''
##### Task 3
Create the user interface described in the image task3.png
using the .grid() method
(3 points)
'''

from tkinter import *
import tkinter as tk

window = tk.Tk()
window.attributes("-topmost",True)
window.title('Example')
window.resizable(False,False)

dogPhoto = PhotoImage(file="dog.png")
descriptionText='A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero'

lable_Photo = tk.Label(window, image=dogPhoto)
lable_Text = tk.Label(window, text='Pochacco!')
lable_Description = tk.Label(window, text=descriptionText, bg="#92e2ed")

lable_Photo.grid(row=0, column=0, sticky=tk.E)
lable_Text.grid(row=0, column=1, sticky=tk.W)
lable_Description.grid(columnspan=2)

window.mainloop()