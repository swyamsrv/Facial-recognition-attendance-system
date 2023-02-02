import tkinter.messagebox
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from employee import Employee
from training import train_classifier
import tkinter
import os
import face_recognition
from attendance import Attendance
from help import Help
from developer import Developer
from datetime import datetime
from time import strftime


class FaceRecognitionSystem:

    def __init__(self, root):
        self.root = root  # Initialization of root
        self.root.geometry('1920x1080')  # Highest screen size resolution
        # self.root.attributes('-fullscreen', True) # Attribute for full screen
        self.root.title("Face Recognition Attendance System")
        self.root.wm_iconbitmap("icon_.ico")


        # BG PICTURE

        img = Image.open("Images//bg2.jpg")
        img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL image
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # Label

        fras = Label(self.root, text='Facial Recognition Attendance System', font=('Blackletter', 25, 'bold'),
                     bg='#0C090A', fg='white')
        fras.place(x=0, y=40, height=50, width=1550)

        # ######### TIME #################
        def time():
            strng = strftime("%H:%M:%S %p")
            lbl.config(text=strng)
            lbl.after(1000, time)

        lbl = Label(fras, font=('times new roman', 14, 'bold'), background='#0C090A', foreground='white')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        # Employee button

        emp_button = Image.open("Images//employee_butt.png")
        emp_button.resize((220, 220), Image.Resampling.LANCZOS)
        self.emp_button = ImageTk.PhotoImage(emp_button)

        b1 = Button(bg_img, image=self.emp_button, cursor='hand2', border=2, relief='raised', bg="#007AFF",
                    command=self.employee_details)
        b1.place(x=120, y=150, width=220, height=220)

        b1_1 = Button(bg_img, text='Employee Details', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, activeforeground='#4681f4',
                      command=self.employee_details)
        b1_1.place(x=120, y=330, width=220, height=40)

        # Face detector

        face_button = Image.open("Images//face_detect1.png")
        face_button.resize((220, 180), Image.Resampling.LANCZOS)
        self.face_button = ImageTk.PhotoImage(face_button)

        b2 = Button(bg_img, image=self.face_button, cursor='hand2', border=2, relief='raised', bg='#ADD8E6',
                    activebackground='#ADD8E6', command=self.face_data)
        b2.place(x=450, y=150, width=220, height=180)

        b2_1 = Button(bg_img, text='Face Detector', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', command=self.face_data, activebackground='#4681f4', border=1, activeforeground='#4681f4')
        b2_1.place(x=450, y=330, width=220, height=40)

        # Attendance

        aten_button = Image.open("Images//attend.jpg")
        aten_button.resize((180, 220), Image.Resampling.LANCZOS)
        self.aten_button = ImageTk.PhotoImage(aten_button)

        b3 = Button(bg_img, image=self.aten_button, cursor='hand2', border=2, relief='raised', bg='#ADD8E6',
                    activebackground='#ADD8E6', command=self.attendance_details)
        b3.place(x=870, y=150, width=220, height=200)

        b3_1 = Button(bg_img, text='Attendance', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, activeforeground='white', command=self.attendance_details)
        b3_1.place(x=870, y=330, width=220, height=40)

        # Help

        help_button = Image.open("Images//hlp.png")
        help_button.resize((220, 180), Image.Resampling.LANCZOS)
        self.help_button = ImageTk.PhotoImage(help_button)

        b4 = Button(bg_img, image=self.help_button, cursor='hand2', border=2, relief='raised', bg='#007AFF',
                    activebackground='#007AFF', command=self.Help)
        b4.place(x=1200, y=150, width=220, height=180)

        b4_1 = Button(bg_img, text='Help?', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, activeforeground='white', command=self.Help)
        b4_1.place(x=1200, y=330, width=220, height=40)

        # Train data

        train_button = Image.open("Images//train_but.png")
        train_button.resize((220, 180), Image.Resampling.LANCZOS)
        self.train_button = ImageTk.PhotoImage(train_button)

        b5 = Button(bg_img, image=self.train_button, cursor='hand2', border=2, relief='raised', bg='#ADD8E6',
                    activebackground='#ADD8E6', command=self.train_data)
        b5.place(x=120, y=500, width=220, height=180)

        b5_1 = Button(bg_img, text='Train Data', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, activeforeground='white', command=self.train_data)
        b5_1.place(x=120, y=680, width=220, height=40)

        # Photos

        photo_button = Image.open("Images//photo_butt.png")
        photo_button.resize((220, 220), Image.Resampling.LANCZOS)
        self.photo_button = ImageTk.PhotoImage(photo_button)
        b6 = Button(bg_img, image=self.photo_button, command=self.open_image, cursor='hand2', border=2, relief='raised', bg= '#007AFF',
                    activebackground='#007AFF')
        b6.place(x=450, y=500, width=220, height=180)

        b6_1 = Button(bg_img, text='Photos', command=self.open_image, font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, activeforeground='white')
        b6_1.place(x=450, y=680, width=220, height=40)

        # Developer

        develop_button = Image.open("Images//develop.png")
        develop_button.resize((220, 180), Image.Resampling.LANCZOS)
        self.develop_button = ImageTk.PhotoImage(develop_button)

        b7 = Button(bg_img, image=self.develop_button, cursor='hand2', border=2, relief='raised', bg='#007AFF',
                    activebackground='#007AFF', command=self.Developer)
        b7.place(x=870, y=500, width=220, height=180)

        b7_1 = Button(bg_img, text='Developer', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, activeforeground='white',command=self.Developer)
        b7_1.place(x=870, y=680, width=220, height=40)

        # Exit

        exit_button = Image.open("Images//exit.png")
        exit_button.resize((220, 220), Image.Resampling.LANCZOS)
        self.exit_button = ImageTk.PhotoImage(exit_button)

        b8 = Button(bg_img, image=self.exit_button, cursor='hand2', border=2, relief='raised', bg='#007AFF',
                    activebackground='#007AFF', command = self.iExit)
        b8.place(x=1200, y=500, width=220, height=180)

        b8_1 = Button(bg_img, text='Exit', font=('sans serif', 15, 'bold'), bg='#4681f4', fg='white',
                      cursor='hand2', activebackground='#4681f4', border=1, command = self.iExit, activeforeground='white')
        b8_1.place(x=1200, y=680, width=220, height=40)

    #  Function Button#####

    def open_image(self):
        os.startfile("data")

    def employee_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Employee(self.new_window)

    def train_data(self):
        self.app3 = train_classifier()

    def face_data(self):
        # self.new_window = Toplevel(self.root)
        # self.app = FaceRec(self.new_window)
        self.app4 = face_recognition.face_recog()
        self.app4.wm_iconbitmap("icon_.ico")



    def attendance_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit this")
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

    def Help(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)
        self.new_window.wm_iconbitmap('web-developing.ico')

    def Developer(self):
        self.new_window = Toplevel(self.root)
        self.app5 = Developer(self.new_window)
        self.new_window.wm_iconbitmap('web-developing.ico')


if __name__ == '__main__':
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

