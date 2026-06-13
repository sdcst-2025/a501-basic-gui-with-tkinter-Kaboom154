'''
##### Task 4
Create the user interface described in the image task3.png
using the .place() method
(3 points)
'''

from tkinter import *
import tkinter as tk

window = tk.Tk()
window.attributes("-topmost",True)
window.title('Example')
window.geometry("257x133")
window.resizable(False,False)

dogPhoto = PhotoImage(file="dog.png")
descriptionText='A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero'

lable_Photo = tk.Label(window, image=dogPhoto)
lable_Text = tk.Label(window, text='Pochacco!')
lable_Description = tk.Label(window, text=descriptionText, bg="#92e2ed")

lable_Photo.place(x=70, y=0)
lable_Text.place(x=134, y=47)
lable_Description.place(x=0, y=96)

window.mainloop()