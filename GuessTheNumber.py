import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import _show

textList = ["Scanning Memory...",
            "Decoding Thoughts...",
            "Analyzing Brain..."
            ]

root= tk.Tk()
root.title("Mind Reader")

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

title = tk.Label(root, text="Think of a number form 1 to 100.")
canvas1.create_window(200, 100, window=title)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

def newWindow1():
    new1= Toplevel(root)
    new1.geometry("250x250")
    new1.title("Reading Your Mind")
    Label(new1, text=textList[0], font=('Helvetica 17 bold')).pack(pady=30)
    new1.after(1000, new1.destroy)

def newWindow2():
    new2= Toplevel(root)
    new2.geometry("250x250")
    new2.title("Reading Your Mind")
    Label(new2, text=textList[1], font=('Helvetica 17 bold')).pack(pady=30)
    new2.after(1000, new2.destroy)

def newWindow3():
    new3= Toplevel(root)
    new3.geometry("250x250")
    new3.title("Reading Your Mind")
    Label(new3, text=textList[2], font=('Helvetica 17 bold')).pack(pady=30)
    new3.after(1000, new3.destroy)

def open_win():
    x1 = entry1.get()

    root.after(2000, newWindow1)
    root.after(4000, newWindow2)
    root.after(6000, newWindow3)
    root.after(8000,lambda : _show('I Read Your Mind', 'You were thinking of ' + str(x1)))
    
button1 = tk.Button(text='Read My Mind', command=open_win)
canvas1.create_window(200, 180, window=button1)

root.mainloop()