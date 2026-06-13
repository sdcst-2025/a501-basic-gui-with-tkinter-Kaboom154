'''
##### Task 2
Create the user interface described in the image task2.png.
This image was created using the .grid() method, but you can
use .pack() or .place() also
(5 points)
'''

from tkinter import *
import tkinter as tk

window = tk.Tk()
window.attributes("-topmost",True)
window.title('T-Town Veterinary Clinic Datsabase')

dogPhoto = PhotoImage(file="dog.png")


lable_photo = tk.Label(window, image=dogPhoto)
lable_Title = tk.Label(window, text='Client Database')
lable_Name = tk.Label(window, text='Name')
lable_Type = tk.Label(window, text='Type')
lable_Breed = tk.Label(window, text='Breed')
lable_Owner = tk.Label(window, text='Owner')
lable_Birthdate = tk.Label(window, text='Birthdate')

entry_Search = tk.Entry(window)
entry_Name = tk.Entry(window, width=14)
entry_Type = tk.Entry(window, width=14)
entry_Breed = tk.Entry(window, width=14)
entry_Owner = tk.Entry(window, width=14)
entry_birthdate = tk.Entry(window, width=14)

button_Previous = tk.Button(window, text='< Previous')
button_Next = tk.Button(window, text='Next >')
button_Save = tk.Button(window, text='Save Entry', height=2)
button_Search = tk.Button(window, text='Search by Name')

lable_photo.grid(row=0, column=0, rowspan=3)
lable_Title.grid(row=1, column=2, sticky=tk.N)
button_Search.grid(row=0, column=3, sticky=tk.N)
entry_Search.grid(row=0, column=4, pady=4, sticky=tk.N)

lable_Name.grid(row=3, column=0)
entry_Name.grid(row=4, column=0, padx=2, pady=2)
lable_Type.grid(row=3, column=1)
entry_Type.grid(row=4, column=1, padx=2, pady=2)
lable_Breed.grid(row=3,column=2)
entry_Breed.grid(row=4, column=2, padx=2, pady=2)
lable_Owner.grid(row=3, column=3)
entry_Owner.grid(row=4, column=3, padx=2, pady=2)
lable_Birthdate.grid(row=3, column=4)
entry_birthdate.grid(row=4, column=4, padx=2, pady=2)

button_Previous.grid(row=5, column=0, padx=1, sticky=tk.W)
button_Save.grid(row=5, column=2, pady=2)
button_Next.grid(row=5, column=4, padx=1, sticky=tk.E)

window.mainloop()