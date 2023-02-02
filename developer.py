from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration')
        self.root.geometry('1200x400+200+100')
        self.root.wm_iconbitmap("icon_.ico")

        # # Frame
        #
        # main_frame = Frame(self.root, bd=2)
        # main_frame.place(x=50, y=50, width=900, height=475)

        # img = Image.open("Images//bg1.jpg")
        # img = img.resize((1000, 600), Image.Resampling.LANCZOS)
        # self.photoimg = ImageTk.PhotoImage(img)
        # # ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL image
        # bg_img = Label(self.root, image=self.photoimg)
        # bg_img.place(x=0, y=10, relwidth=1, relheight=1)


        # Label
        fras = Label(self.root, text='Developer', font=('Blackletter', 25, 'bold'),
                      fg='black')
        fras.place(x=585, y=20, height=40, width=160)

        # Developer info

        img2 = Image.open("Images//mine_image.png")
        img2 = img2.resize((220, 220), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        bg_img2 = Label(self.root, image=self.photoimg2)
        bg_img2.place(x=50, y=40, height=220, width=220)

        # Label

        f_labl = Label(self.root, text='Hey there!\nMy Name is Swyam Srivastava,\nA final year Engineering Student\n'
                                       'This project is initiated by me during my internship at \nsahara next', font=('Arial', 20, 'bold'))
        f_labl.place(x=300, y=100)

        # Image

        img3 = Image.open("Images//logo1.png")
        img3 = img3.resize((150, 70), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img3 = Label(self.root, image=self.photoimg3)
        bg_img3.place(x=580, y=280, height=70, width=150)


if __name__ == '__main__':
    root = Tk()
    obj = Developer(root)
    root.mainloop()
