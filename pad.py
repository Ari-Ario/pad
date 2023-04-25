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
        self.c.bind("<B1-Motion>", self.draw)
        self.c.bind("<ButtonRelease-1>", self.reset)
    
    # method to draw the line
    def draw(self, e):
        if self.pre_x and self.pre_y:
            self.c.create_line(self.pre_x, self.pre_y, e.x, e.y, width=self.brush_width,
                               fill=self.col_fg, capstyle="round")
        self.pre_x = e.x
        self.pre_y = e.y
    
    #method to reset the brush to paint a new line
    def reset(self, e):
        self.pre_x= None
        self.pre_y= None

    # a mthod to draw linked lines by points
    def continuous(self, e):
        self.pre_x= e.x
        self.pre_y= e.y

    #method to modify the brush-size
    def brush_change(self, width):
        self.brush_width = width
    
    #method to change brush-color
    def brush_color(self):
        color = colorchooser.askcolor()[1]
        self.col_fg= color

    #method to change background-color of the pad
    def backgound_color(self):
        color = colorchooser.askcolor()[1]
        self.c["bg"]= color

    #method to clear the board
    def clear_pad(self):
        self.c.delete(ALL)

    #all labels, frames, canvas, filemenu, etc. within this method
    def draw_widgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        textpw = Label(self.controls, text="Pen Width")
        textpw.grid(row=0, column=0)
        self.slider= ttk.Scale(self.controls, from_=5, to=100, command=self.brush_change)
        self.slider.set(self.brush_width)
        self.slider.grid(row=1, column=0)
        self.controls.pack(side=LEFT)
        self.c = Canvas(self.master, bg=self.col_bg)
        self.c.pack(fill=BOTH, expand=True)
        #menu
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        #file-menu
        filemeu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemeu)
        filemeu.add_command(label="Save As", command=None)
        filemeu.add_command(label="Import", command=None)
        filemeu.add_command(label="Exit", command=self.master.destroy)
        #edit-menu
        editmenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Brush Color", command=self.brush_color)
        editmenu.add_command(label="BG Color", command=self.backgound_color)
        editmenu.add_command(label="Clear Pad", command=self.clear_pad)
        #geometry-menu
        geometrymenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Insert", menu=geometrymenu)
        geometrymenu.add_command(label="Line" , command=None)
        geometrymenu.add_command(label="Circle" , command=None)
        geometrymenu.add_command(label="Triangular" , command=None)


if __name__ == "__main__":
    root = Tk()
    root.title("PADY")
    main(root)
    root.mainloop()