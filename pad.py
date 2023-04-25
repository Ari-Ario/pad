"""A simple pad with diffrent function"""

import tkinter
from tkinter import *
from tkinter import ttk, messagebox, colorchooser

root = Tk()
root.title("PADY")
root.geometry("700x500")
l_frame= LabelFrame(root, text="Draw on the pad")
l_frame.grid(row=0, column=0)
c = Canvas(l_frame, background="light cyan", width=700, height=450)
c.grid(row=0, column=0)

root.mainloop()