"""A simple pad with diffrent function"""

import tkinter
from tkinter import *
from tkinter import ttk, messagebox, colorchooser

#in oop: class instead functional pro.
class main:
    def __init__(self, master):
        self.master = master
        self.col_fg = "black"
        self.col_bg = "cyan"
        self.pre_x = None
        self.pre_y = None
        self.brush_width= 5
        self.draw_widgets()
    
    def paint(self):
        pass

    def draw_widgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        textpw = Label(self.controls, text="Pen Width")
        textpw.grid(row=0, column=0)
        self.slider= ttk.Scale(self.controls, from_=5, to=100, command=None)
        self.slider.set(self.brush_width)
        self.slider.grid(row=1, column=0)
        self.controls.pack(side=LEFT)
        self.c = Canvas(self.master, bg=self.col_bg)
        self.c.pack(fill=BOTH, expand=True)
        #menu
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        filemeu= Menu(menubar)
        menubar.add_cascade(label="Menu", menu=filemeu)


if __name__ == "__main__":
    root = Tk()
    root.title("PADY")
    main(root)
    root.mainloop()