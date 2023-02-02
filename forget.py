import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class ForgetPassword:

    def __init__(self, root):
        self.root = root
        self.root.geometry('400x300+470+200')
        self.root.config(bg='#4a7a8c')
        self.root.title('Forgotten Password')
        self.root.wm_iconbitmap("icon_.ico")
        self.var_email = StringVar()
        self.var_seq_ans = StringVar()

        # email

        eml_label = Label(self.root, text='Enter your email', font=('Times New Roman', 15, 'bold'), bg='#4a7a8c')
        eml_label.place(x=50, y=50)

        # input for email

        self.email = ttk.Entry(self.root, textvariable=self.var_email, font=('Sans serif', 15, 'bold'))
        self.email.place(x=50, y=115, width=275)

        butt = Button(self.root, text='Proceed', font=('Sans serif', 15, 'bold'), bg='#263E49',
                      activebackground='#263E49', cursor='hand2', command=self.forgotten_pass_window)
        butt.place(x=50, y=205, width=100)

    def forgotten_pass_window(self):
        if self.var_email.get().strip(" ") == "":
            messagebox.showerror("Error!", "Please Write the email to reset password")
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='Ssrv@005', database = 'swym')
            my_cursor = conn.cursor()
            query = ("select * from swym.login_register where e_mail=%s")
            my_cursor.execute(query, (self.var_email.get().strip(" "),))
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror('Error', "Please Enter the valid Email")
            else:
                query = ("select sec_ques, sec_ans, password from swym.login_register where e_mail=%s")
                my_cursor.execute(query, (self.var_email.get().strip(" "),))
                row = my_cursor.fetchone()
                self.ques = row[0]
                self.ans = row[1]
                self.password = row[2]
                conn.close()

                # 2nd window for security question

                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry('400x400+470+200')
                self.root2.config(bg='#4a7a8c')

                sequrity_Q = Label(self.root2, text='Security Question', font=('sans serif', 15, 'bold'), bg='#4a7a8c')
                sequrity_Q.place(x=60, y=20)
                self.Sequrity_Q = ttk.Label(self.root2, text=self.ques, font=('Sans serif', 15, 'bold'))
                self.Sequrity_Q.place(x=60, y=80, width=240)

                # Security Answer

                sequrity_A = Label(self.root2, text='Security Answer', font=('sans serif', 15, 'bold'), bg='#4a7a8c')
                sequrity_A.place(x=60, y=140)
                self.Sequrity_A = ttk.Entry(self.root2, textvariable=self.var_seq_ans, font=('Sans serif', 15, 'bold'))
                self.Sequrity_A.place(x=60, y=190, width=240)

                # BUtton for get pass

                butt = Button(self.root2, text='Check Password', font=('Sans serif', 15, 'bold'), bg='#263E49',
                              activebackground='#263E49', cursor='hand2', command=self.check)
                butt.place(x=50, y=250, width=250)

    def check(self):

        if self.var_seq_ans.get().lower() == self.ans.lower():
            pss = Label(self.root2, text="Your Password is '{}'".format(self.password),
                        font=('times new roman', 15, 'bold'), bg='#4a7a8c')
            pss.place(x=60, y=320)

        else:
            messagebox.showerror("Wrong", "The Answer you entered is wrong.", parent = self.root)
            self.Sequrity_A.delete(0, END)
            self.root2.destroy()


if __name__ == '__main__':
    root = Tk()
    obj = ForgetPassword(root)
    root.mainloop()