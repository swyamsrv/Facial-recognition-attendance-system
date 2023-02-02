from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Help:

    def __init__(self, root):
        self.root = root
        self.root.title('Help')
        self.root.geometry('525x300+470+200')
        self.root.config(bg='#4681f4')
        self.root.wm_iconbitmap("icon_.ico")


        # Frame

        main_frame = Frame(self.root, bd=0, bg='#4681f4')
        main_frame.place(x=50, y=70, width=425, height=150)

        # Label Frame

        hlp = Label(main_frame, text="For any help\nSend me your query at \n'swyamsrv05@gmail.com'", bg='#4681f4', font=("Arial", 20,"bold"))
        hlp.grid(row=0, column=1, pady=20, padx=30)


if __name__ == '__main__':
    root = Tk()
    obj = Help(root)
    root.mainloop()