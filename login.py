import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from register import Register
from main import FaceRecognitionSystem
from forget import ForgetPassword


def main():
    win = Tk()
    app = Login(win)
    win.mainloop()


class Login:

    def __init__(self, root):
        self.root = root  # Initialization of root
        self.root.title("Face Recognition Attendance System")
        self.root.geometry('1920x1080')  # Highest screen size resolution
        self.root.wm_iconbitmap("icon_.ico")
        # self.root.attributes('-fullscreen', True) # Attribute for full screen

        # BG PICTURE
        img = Image.open("Images//wallpaperflare.com_wallpaper.jpg")
        img = img.resize((1650, 900), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL image
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # 1st Image
        img1 = Image.open("Images//imG_REC.jpg")
        img1 = img1.resize((150, 150), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_label = Label(self.root, image=self.photoimg1)
        f_label.place(x=0, y=0, width=150, height=150)

        # Login frame
        frame = Frame(self.root, bg='#4a7a8c', border=5, relief='sunken')
        frame.place(x=1000, y=150, width=375, height=500)

        # USER_login_image

        log_img = Image.open('Images//user_login.png')
        log_img.resize((200, 130), Image.Resampling.LANCZOS)
        self.photoimg_userlog = ImageTk.PhotoImage(log_img)
        login_user_label = Label(frame, image=self.photoimg_userlog, bg='#4a7a8d')
        login_user_label.place(x=85, y=0, width=200, height=130)

        # WELCOME

        get_str = Label(frame, text="WELCOME", font=('TIMES NEW ROMAN', 20, 'bold'), fg='#9fafca', bg='#4a7a8c')
        get_str.place(x=105, y=115)

        # Label for username

        username_lbl = Label(frame, text='E-MAIL', font=('SANS SERIF', 20, 'bold'), bg='#4a7a8d')
        username_lbl.place(x=55, y=175)

        # Image for username

        username_icon = Image.open('Images//icons8-name-48.png')
        username_icon.resize((40, 40), Image.Resampling.LANCZOS)
        self.username_icon = ImageTk.PhotoImage(username_icon)
        username_icon_lbl = Label(frame, image=self.username_icon, bg='#4a7a8d')
        username_icon_lbl.place(x=10, y=175, width=40, height=40)

        # Entry for username

        self.user_name = ttk.Entry(frame, font=('SANS SERIF', 15, "bold"))
        self.user_name.place(x=15, y=230, width=320)

        # Label for password

        userpass_lbl = Label(frame, text='PASSWORD', font=('SANS SERIF', 20, "bold"), bg='#4a7a8d')
        userpass_lbl.place(x=55, y=280)

        # Image for password

        password_icon = Image.open('Images//icons8-password-48.png')
        password_icon.resize((35, 35), Image.Resampling.LANCZOS)
        self.password_icon = ImageTk.PhotoImage(password_icon)
        password_icon_lbl = Label(frame, image=self.password_icon, bg='#4a7a8d')
        password_icon_lbl.place(x=10, y=272, width=40, height=45)

        # Entry for password
        self.user_pass = ttk.Entry(frame, font=('SANS SERIF', 15, "bold"), show='*')
        self.user_pass.place(x=15, y=335, width=320)

        # LOGIN BUTTON

        # login_img = Image.open('Images/icons8-enter-48.png')
        # login_img.resize((48, 150), Image.Resampling.LANCZOS)
        # self.login_img= ImageTk.PhotoImage(login_img)

        login_buton_lbl = Button(frame,  text='LOGIN', font=('SANS SERIF', 15, 'bold'),  cursor="hand2",  bd=5,
                                  fg='white',  bg='blue', activebackground='blue', activeforeground='white',
                                 command=self.login_function)
        login_buton_lbl.place(x=15, y=395, height=48, width=150)

        # REGISTER BUTTON

        registerbtn = Button(frame, text='New User?\nRegister', font=('SANS SERIF', 10, 'bold'), border=0,
                             bg='#4a7a8d', fg='white', activebackground='#4a7a8d', cursor="hand2",
                             command=self.register_window)
        registerbtn.place(x=240, y=400, height=40, width=100)

        # FORGET BUTTON

        forgetbtn = Button(frame, text='Forget Password', font=('SANS SERIF', 13), border=0, bg='#4a7a8d',
                             fg='white', activebackground='#4a7a8d', cursor="hand2", command=self.forget_window)
        forgetbtn.place(x=10, y=450, height=20, width=160)

    def register_window(self):
        self.new_window = Toplevel(self.root)  # If a application needs to represent some extra information, pop up,
        # or the group of widgets on the new window
        self.app = Register(self.new_window)

    def forget_window(self):
        self.forget = Toplevel(self.root)
        self.app2 = ForgetPassword(self.forget)

    def login_function(self):

        if self.user_name.get() == "" and self.user_pass.get() == "":
            messagebox.showerror("Error!", "All Field Required")
        elif self.user_name.get() == 'Swyam05' and self.user_pass.get() == '123456789':
            messagebox.showinfo("WELCOME", "You're welcome")
        else:
            # messagebox.showerror('Error', 'Please Enter correct username or password')
            conn = mysql.connector.connect(host='localhost', user='root', password="Ssrv@005", database = 'swym')
            my_cursor = conn.cursor()
            my_cursor.execute('select * from swym.login_register where e_mail = %s and password = %s', (
                                                                                                self.user_name.get(),
                                                                                                self.user_pass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error!", "Invalid username and password")
                self.user_name.delete(0, END)
                self.user_pass.delete(0, END)
            else:
                open_main = messagebox.askyesno("Yes or No", "Welcome back!!\nContinue")
                if open_main > 0:
                    self.user_name.delete(0, END)
                    self.user_pass.delete(0, END)
                    self.new_window = Toplevel(self.root)
                    self.app = FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()


if __name__ == '__main__':
    main()