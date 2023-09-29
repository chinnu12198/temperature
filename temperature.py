import tkinter as tk
import random 
import string
from tkinter.ttk import Button
from tkinter import Entry
from tkinter.ttk import Spinbox
from tkinter.ttk import Label
import os
gui = tk.Tk()
gui.geometry('300x300')
gui.title("Random Password Generator")
output = tk.StringVar()
all = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]

def randPassGen():
    password = "" 
    for y in range(pass_len.get()):
        char_type = random.choice(all)
        password = password + random.choice(char_type) 
    output.set(password)

def copyPass():
    os.copy(output.get())

pass_head = Label(gui, text = 'Password Length', font = 'arial 10 bold').pack(pady=10)

pass_len = tk.IntVar()

length = Spinbox(gui, from_ = 0, to_ = 8 , textvariable = pass_len , width = 40, font='arial 15 bold').pack()

Button(gui, command = randPassGen, text = "Generate Password" ).pack(pady= 20)

pass_label = Label(gui, text = 'Random Generated Password').pack(pady="40 20")

Entry(gui , textvariable = output, width = 40,font='arial 15 bold').pack()

Button(gui, text = 'Copy to Clipboard', command = copyPass).pack(pady= 40)

gui.mainloop()