import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title('Registration')
        self.root.geometry('1920x1080')
        self.root.config(bg='WHITE')
        self.root.wm_iconbitmap("icon_.ico")


        # ########Variables###########

        self.var_fname = StringVar()
        self.var_mname = StringVar()
        self.var_lname = StringVar()
        self.var_mob = StringVar()
        self.var_age = StringVar()
        self.var_email = StringVar()
        self.var_seq_ques = StringVar()
        self.var_seq_ans = StringVar()
        self.var_password = StringVar()
        self.var_cnfrm_password = StringVar()
        self.var_gender = StringVar()

        # ######## bg_Image #######

        # bg_img = Image.open("Images//register_bg.jpg")
        # bg_img = bg_img.resize((1650, 900), Image.Resampling.LANCZOS)
        # self.bg_img = ImageTk.PhotoImage(bg_img)
        # bg_label = Label(self.root, image=self.bg_img)
        # bg_label.place(x=0, y=0, relheight=1, relwidth=1)

        # Frame
        frame = Frame(self.root, bg='#4a7a8c', border=2, relief= 'groove')
        frame.place(x=118, y=150, width=1300, height=600)

        # Registration

        reg_img = Image.open('Images//register.png')
        reg_img = reg_img.resize((343, 77), Image.Resampling.LANCZOS)
        self.Reg_img = ImageTk.PhotoImage(reg_img)
        Reg_img = Label(self.root, image=self.Reg_img, bg='WHITE')
        Reg_img.place(x=600, y=50, width=343, height=77)

        # First name

        frst_name = Label(frame, text="First Name", fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        frst_name.place(x=40, y=30, width=150)

        self.first_name = ttk.Entry(frame, textvariable=self.var_fname, font=('Times New Roman', 15, "bold"))
        self.first_name.place(x=60, y=80, width=240)

        # Middle name

        mid_name = Label(frame, text="Middle Name", fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        mid_name.place(x=500, y=30, width=150)

        self.mid_name = ttk.Entry(frame,textvariable=self.var_mname, font=('Sans serif', 15, "bold"))
        self.mid_name.place(x=510, y=80, width=240)

        # Last Name

        last_name = Label(frame, text='Last Name', fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        last_name.place(x=950, y=30, width=150)

        self.last_name = ttk.Entry(frame, textvariable=self.var_lname, font=('Times New Roman', 15, "bold"))
        self.last_name.place(x=970, y=80, width=240)

        # Mobile no

        mob_no = Label(frame, text="Mobile Number", fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        mob_no.place(x=60, y=170, width=150)

        self.mob_no = ttk.Entry(frame, textvariable=self.var_mob, font=('Sans serif', 15, 'bold'))
        self.mob_no.place(x=60, y=220, width=240)

        # Email id

        email = Label(frame, text="Email Id", fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        email.place(x=940, y=170, width=150)

        self.email = ttk.Entry(frame, textvariable=self.var_email, font=('Sans serif', 15, 'bold'))
        self.email.place(x=970, y=220, width=240)

        # Age

        age = Label(frame, text="Age", fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        age.place(x=500, y=170, width=80)

        self.age = ttk.Entry(frame, textvariable=self.var_age, font=('Sans serif', 15, 'bold'))
        self.age.place(x=510, y=220, width=240)

        # Gender

        gendr = Label(frame, text='Gender', fg='black', bg='#4a7a8c', font=('Sans serif', 15, 'bold'))
        gendr.place(x=940, y=310, width=150)

        self.cmb_gender = ttk.Combobox(frame, font=("sans serif", 14), textvariable=self.var_gender,
                                       state='readonly', justify=CENTER, cursor='hand2')
        self.cmb_gender['values'] = ("Select", "Male", "Female", "Other")
        self.cmb_gender.current(0)
        self.cmb_gender.place(x=970, y=360)

        # radio1 = Radiobutton(frame, text='Male', variable=self.var_gender, value=1, font=('Sans serif', 14, 'bold'),
        #                      bg='#4a7a8c', activebackground='#4a7a8c', cursor='hand2')
        # radio1.place(x=975, y=360)
        # radio2=Radiobutton(frame, text='Female', variable=self.var_gender, value=2,  font=('Sans serif', 14, 'bold'),
        #                      bg='#4a7a8c', activebackground='#4a7a8c', cursor='hand2')
        # radio2.place(x=1075, y=360)
        #
        # radio3 = Radiobutton(frame, text='Other', variable=self.var_gender, value=3, font=('Sans serif', 14, 'bold'),
        #                      bg='#4a7a8c', activebackground='#4a7a8c', cursor='hand2')
        # radio3.place(x=1175, y=360)

        # Security question

        sequrity_Q = Label(frame, text='Security Question', font=('sans serif', 15, 'bold'), bg='#4a7a8c')
        sequrity_Q.place(x=60, y=310)

        self.Sequrity_Q = ttk.Combobox(frame, textvariable=self.var_seq_ques, font=('Sans serif', 15, 'italic'),
                                       state='readonly', cursor='hand2', justify=CENTER)
        self.Sequrity_Q['values'] = ("Select", "Your Best Friend Name", "Your Birth Place", "Your First School Name",
                                     "Your Pet Name")
        self.Sequrity_Q.place(x=60, y=360, width=240)
        self.Sequrity_Q.current(0)

        # Security Answer

        sequrity_A = Label(frame, text='Security Answer', font=('sans serif', 15, 'bold'), bg='#4a7a8c')
        sequrity_A.place(x=510, y=310)

        self.Sequrity_A = ttk.Entry(frame, textvariable=self.var_seq_ans, font=('Sans serif', 15, 'bold'))
        self.Sequrity_A.place(x=510, y=360, width=240)

        # Password

        password = Label(frame, text='Password', font=('Sans serif', 15, 'bold'), bg='#4a7a8c')
        password.place(x=60, y=450)

        self.password = ttk.Entry(frame, textvariable=self.var_password, font=('Sans serif', 15, 'bold'), show='*')
        self.password.place(x=60, y=500, width=240)

        # Confirm Password

        confrm_password = Label(frame, text='Confirm Password', font=('Sans serif', 15, 'bold'), bg='#4a7a8c')
        confrm_password.place(x=510, y=450)

        self.confrm_password = ttk.Entry(frame, textvariable=self.var_cnfrm_password, font=('Sans serif', 15, 'bold'),
                                         show='*')
        self.confrm_password.place(x=510, y=500, width=240)

        # Register button

        reg_butt = Image.open('Images//reg_but.png')
        reg_butt.resize((250, 94), Image.Resampling.LANCZOS)
        self.reg_butt = ImageTk.PhotoImage(reg_butt)
        reg_butt_lbl = Button(frame, image=self.reg_butt, command=self.register_data, bg='#4a7a8c', border=0,
                              activebackground='#4a7a8c',
                              cursor='hand2')
        reg_butt_lbl.place(x=850, y=455, height=94, width=250)

        # Already
        already = Label(frame, text='Already\n Registered?', font=('Sans serif', 10, 'bold'), border=0,
                             bg='#4a7a8d', fg='black', activebackground='#4a7a8d')
        already.place(x=1130, y=470)

        # LOGIN button

        login = Button(frame, text='Log In', font=('Sans serif', 10), fg = 'white', bg='#4a7a8d', border=0,
                       activebackground='#4a7a8d', cursor='hand2', activeforeground='black', command=self.return_login)
        login.place(x=1150, y=510)

    # #### Function declaration ####

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_seq_ques.get() == "Select" or \
                self.var_seq_ans.get() == "" or self.var_age.get() == 0 or self.var_gender.get() == 'Select':
            messagebox.showerror('Error!', 'Please Fill the requirement details')

        elif self.var_password.get() != self.var_cnfrm_password.get():
            messagebox.showerror("Error!", "Password must be same")
            self.password.delete(0, END)
            self.confrm_password.delete(0, END)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Ssrv@005", database="swym")
                # Connecting the database from the server....
                my_cursor = conn.cursor()  # creating an instance of 'cursor' class which is used to execute
            # the 'SQL' statements in 'Python'
                query = ("select * from swym.login_register where e_mail=%s")
                # values = (self.var_email.get(), )
                my_cursor.execute(query, (self.var_email.get(),))
                row = my_cursor.fetchone()
                if row != None:
                    messagebox.showerror("Error", 'User already exist\nplease try another email')

                # my_cursor.execute("select * from swym.login_register where e_mail=%s", self.var_email.get())
                # row = my_cursor.fetchone()
                # if row != None:
                #     messagebox.showerror("Error !", "Already Exists Email ! Try with another one.", parent=self.root)
                else:
                    my_cursor.execute("insert into swym.login_register (fname, mname, lname, mob_number, age, e_mail, "
                                      "sec_ques, sec_ans, password, gender) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                      (self.var_fname.get(), self.var_mname.get(), self.var_lname.get(),
                                       self.var_mob.get(),self.var_age.get(), self.var_email.get(),
                                       self.var_seq_ques.get(), self.var_seq_ans.get(), self.var_password.get(),
                                       self.var_gender.get()))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "{} Registered".format(self.var_fname.get()))

            except Exception as e:
                messagebox.showerror("Error", f"Error due to : {str(e)}")

    def return_login(self):
        self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj2 = Register(root)
    root.mainloop()