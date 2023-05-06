"""A simple pad with diffrent function"""

import tkinter
from tkinter import *
from tkinter import ttk, messagebox, colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

#in oop: class instead functional pro.
class main:
    def __init__(self, master):
        self.master = master
        self.col_fg = "black"
        self.col_bg = "light cyan"
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


    #method to creat a line
    def coordinates_win(self):
        self.win_coor = Tk()
        self.win_coor.mainloop
        self.win_coor.title("Coordinates")
        label_x1 = Label(self.win_coor, text="   X1 --\N{RIGHTWARDS ARROW}", width=10).grid(row=0, column=0)
        label_y1 = Label(self.win_coor, text="   Y1 --\N{RIGHTWARDS ARROW}", width=10).grid(row=1, column=0)
        label_x2 = Label(self.win_coor, text="   X2 --\N{RIGHTWARDS ARROW}", width=10).grid(row=2, column=0)
        label_y2 = Label(self.win_coor, text="   Y2 --\N{RIGHTWARDS ARROW}", width=10).grid(row=3, column=0)
        self.entry_x1 = Entry(self.win_coor, width=10)
        self.entry_x1.grid(row=0, column=1)
        self.entry_y1 = Entry(self.win_coor, width=10)
        self.entry_y1.grid(row=1, column=1)
        self.entry_x2 = Entry(self.win_coor, width=10)
        self.entry_x2.grid(row=2, column=1)
        self.entry_y2 = Entry(self.win_coor, width=10)
        self.entry_y2.grid(row=3, column=1)
        #two buttons, which splits the functionality of inserting line and oval by licking on them
        but_insert_line= Button(self.win_coor, text="Insert line", relief=RAISED, command= self.get_line)
        but_insert_line.grid(row=4, column=0, sticky=NSEW)
        but_insert_oval= Button(self.win_coor, text="Insert Oval", relief=RAISED, command= self.get_oval)
        but_insert_oval.grid(row=4, column=1, sticky=NSEW)
        but_insert_rectangle= Button(self.win_coor, text="Insert Rectangle", relief=RAISED, command=self.get_rect)
        but_insert_rectangle.grid(row=5, column=0, sticky=NSEW)

        but_cancel= Button(self.win_coor, text="Quit\N{RIGHTWARDS ARROW}", fg="red", relief=RAISED, command=self.win_coor.destroy)
        but_cancel.grid(row=5, column=1, columnspan=1, sticky=NSEW)

    #this method is bound with the button insert as |
    def get_line(self):
        self.x1= self.entry_x1.get()
        self.y1= self.entry_y1.get()
        self.x2= self.entry_x2.get()
        self.y2= self.entry_y2.get()
        if self.x1 and self.x2 and self.y1 and self.y2:
            self.c.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.col_fg, width=self.brush_width)
            self.win_coor.destroy()
            self.reset("<ButtonRelease-1>")
        else:
            messagebox.showerror("Error", "please fill in all coordinates or press Quit.")
    #this method is bound with the button insert as O
    def get_oval(self):
        self.x1= self.entry_x1.get()
        self.y1= self.entry_y1.get()
        self.x2= self.entry_x2.get()
        self.y2= self.entry_y2.get()
        if self.x1 and self.x2 and self.y1 and self.y2:
            self.c.create_oval(self.x1, self.y1, self.x2, self.y2, fill=self.col_fg, offset="nw", width=self.brush_width)
            self.win_coor.destroy()
            self.reset("<ButtonRelease-1>")
        else:
            messagebox.showerror("Error", "please fill in all coordinates or press Quit.")

    #method to get rectangle
    def get_rect(self):
        self.x1= self.entry_x1.get()
        self.y1= self.entry_y1.get()
        self.x2= self.entry_x2.get()
        self.y2= self.entry_y2.get()
        if self.x1 and self.x2 and self.y1 and self.y2:
            self.c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=self.col_fg, offset="nw", width=self.brush_width)
            self.win_coor.destroy()
            self.reset("<ButtonRelease-1>")
        else:
            messagebox.showerror("Error", "please fill in all coordinates or press Quit.")
    
    #method of the window to open as popup to enter the coordinates of polygone
    def polygone_window(self):
        self.win_poly= Tk()
        self.win_poly.title("Enter Coordinates")
        label_description= Label(self.win_poly, text="Enter 6 numbert (3 tuples) for triangular and more for polygone!")
        label_description.grid(row=0, column=0, columnspan=2)
        label_eg= Label(self.win_poly, text="eg.: 100, 100, 120, 100, 140, 120, 120, 140, 100, 140, 220, 200 ...")
        label_eg.grid(row=1, column=0)
        self.entry_coordinates= Entry(self.win_poly, width=70)
        self.entry_coordinates.grid(row=2, column=0)
        
        but_enter= Button(self.win_poly, text="Enter", command=self.get_poly)
        but_enter.grid(row=3, column=0, sticky=W)
        but_quit= Button(self.win_poly, text="Quit", fg="red", command=self.win_poly.destroy)
        but_quit.grid(row=3, column=0, sticky=E)

    #method of polygone-creator
    def get_poly(self):
        self.nums= self.entry_coordinates.get()
        points= self.nums.split(",")
        lst = []
        for i in points:
            lst.append(int(i))
        if len(lst)>=6:
            self.c.create_polygon(lst, fill=self.col_fg, width=self.brush_width)
            self.win_poly.destroy()
            self.reset("<ButtonRelease-1>")
        else:
            messagebox.showerror("entry error", "Perhaps not numbers or no comma or sum of coordinates are less than 6!")

    #method of popup-creator
    def do_popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    #method to save the Pad
    def save_as_img(self):
        self.win_save_as= Tk()
        self.win_save_as.title("Enter filename")
        self.entry_save_as = Entry(self.win_save_as)
        self.entry_save_as.grid(row=0, column=0)
        self.butt_save_as= Button(self.win_save_as, text="Save", command=self.get_img)
        self.butt_save_as.grid(row=0, column=1)
        self.butt_quit_save= Button(self.win_save_as, text="Quit and back to Pad")
        self.butt_quit_save.grid(row=2, column=1, columnspan=1, sticky=NSEW)

    #method to save the photo as soon as clicking the butt_save_as
    def get_img(self, filename="temp"):
        self.win_save_as.title("Wait, saving image!")
        filename= self.entry_save_as.get()
        self.c.postscript(file=f"{filename}.ps", colormode="color")
        process= subprocess.Popen(["ps2pdf",f"{filename}.ps", "result.pdf"], shell=True)
        process.wait(2)
        self.win_save_as.destroy()

    def import_img(self):
        path = askopenfilename(title="name",defaultextension="*.*", filetypes=[("All Files", "*.*"), ("JPG", ".jpg")])
        if not path:
            return messagebox.showerror("Path Problem","Path does not exist")
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.c.create_image(20, 20, anchor=NW, image=self.img)
        self.c.Image= self.img
    
    #Method of a new popup window to get set new entries
    def chart_win(self):
        self.charwindow= Tk()
        self.charwindow.title("Enteies of chart")
        self.label_item_num= Label(self.charwindow , text="Number of entries:")
        self.entry_item_num= Entry(self.charwindow, width=10)
        self.button_item= Button(self.charwindow ,text="Enter", command=self.set_char)

        self.charwindow.grid()
        self.label_item_num.grid(row=0, column=0)
        self.entry_item_num.grid(row=0, column=1)
        self.button_item.grid(row=0, column=2)

    #Method to set the char with new entries etc.
    def set_char(self):
        self.entry_num = int(self.entry_item_num.get())
        label_names= Label(self.charwindow, text="Enter words:  ")
        label_numbers= Label(self.charwindow, text="Enter numbers:  ")
        butt_insert= Button(self.charwindow, text="Insert Chart", bg="green", command=self.get_char)
        butt_quit= Button(self.charwindow, text="Quit", command=self.charwindow.destroy)
        for i in range(self.entry_num):
            self.name_entries = Entry(self.charwindow, width=10)
            self.num_etries= Entry(self.charwindow, width=10)
            self.name_entries.grid(row=1, column= i+1)
            self.num_etries.grid(row=2, column= i+1)
        #gird of the new labels and buttons
        label_names.grid(row=1, column=0, sticky=E)
        label_numbers.grid(row=2, column=0, sticky=E)
        butt_insert.grid(row=3, column=0)
        butt_quit.grid(row=3, column=1)

    #Method to get the entries of char
    def get_char(self):
        lst= []
        for i in range(self.entry_num):
            lst.append(self.name_entries.get())
        print(lst)

    #all labels, frames, canvas, filemenu, etc. within this method
    def draw_widgets(self):
        self.controls = Frame(self.master, padx=5, pady=5)
        textpw = Label(self.controls, text="Pen Width")
        textpw.grid(row=0, column=0, sticky=N)
        self.slider= ttk.Scale(self.controls, from_=5, to=100, command=self.brush_change)
        self.slider.set(self.brush_width)
        self.slider.grid(row=1, column=0, sticky=N, pady=5)
        self.charts= Button(self.controls, text="Insert Chart", command=self.chart_win)
        self.charts.grid(row=2, column=0, sticky=S, pady= 40)
        self.controls.pack(side=LEFT)
        self.c = Canvas(self.master, bg=self.col_bg)
        self.c.pack(fill=BOTH, expand=True)
        #menu
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        #file-menu
        filemeu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemeu)
        filemeu.add_command(label="Save As", command=self.save_as_img)
        filemeu.add_command(label="Import", command=self.import_img)
        filemeu.add_command(label="Exit", command=self.master.destroy)
        #edit-menu
        editmenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="Brush Color", command=self.brush_color)
        editmenu.add_command(label="BG Color", command=self.backgound_color)
        editmenu.add_command(label="Clear Pad", command=self.clear_pad)
        #geometry-menu
        geometrymenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Insert Geo", menu=geometrymenu)
        geometrymenu.add_command(label="Line" , command=self.coordinates_win)
        geometrymenu.add_command(label="Circle" , command=self.coordinates_win)
        geometrymenu.add_command(label="Rectangle" , command=self.coordinates_win)
        geometrymenu.add_separator()
        geometrymenu.add_command(label="Triangular", command=self.polygone_window) #must have another window
        geometrymenu.add_command(label="Polygone", command=self.polygone_window)
        #chartmenu
        chartmenu= Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Chart", menu=chartmenu)
        chartmenu.add_command(label="Open Chart", command=self.chart_win)
        #pop-up menu by right-click
        self.popup_menu = Menu(self.c, tearoff=0)
        #copy menu will be added
        #cut menu will be added
        self.popup_menu.add_command(label="Insert shape", command=self.coordinates_win)
        self.popup_menu.add_command(label="Import image", command=None)
        self.popup_menu.add_cascade(label="Save as", command=self.save_as_img)
        #binding the popup menu with its method above: do_popup
        self.c.bind("<Button-3>", self.do_popup)


if __name__ == "__main__":
    root = Tk()
    root.title("PADY")
    main(root)
    root.mainloop()