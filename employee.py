import time
import employee
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title("Employee Section")
        self.root.wm_iconbitmap("icon_.ico")

        # Variables

        self.var_dep = StringVar()
        self.var_Bsalary = StringVar()
        self.var_shift = StringVar()
        self.var_Job = StringVar()
        self.var_EId = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_gender = StringVar()
        self.var_addr = StringVar()
        self.var_email = StringVar()
        self.var_mob = StringVar()
        self.var_hod = StringVar()


        # BG PICTURE

        img = Image.open("Images//UI_backimage.png")
        img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL image
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # Label
        fras = Label(self.root, text='Facial Recognition Attendance System', font=('Blackletter', 25, 'bold'),
                     bg='#0C090A', fg='white')
        fras.place(x=0, y=10, height=50, width=1600)

        # Frame

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=75, y=100, width=1400, height=650)

        # Left Label Frame

        left_frame = LabelFrame(main_frame, bd=5, relief=RIDGE, text='Employee Data', font=("Sans serif", 15, 'bold'))
        left_frame.place(x=10, y=10, width=680, height=630)

        # IMAGE

        img_left = Image.open("Images//frame_pic.png")
        img_left.resize((660, 180), Image.Resampling.LANCZOS)
        self.img_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.img_left)
        f_lbl.place(x=0, y=0, width=660, height=188)

        # Current branch

        current_course_frame = LabelFrame(left_frame, bd=5, relief=RIDGE, text='Current Branch Information',
                                          font=('sans serif', 10, 'bold'))
        current_course_frame.place(x=0, y=180, width=670, height=120)

        # Department

        dep_label = Label(current_course_frame, text='Department', font=("sans serif", 10, 'bold'))
        dep_label.grid(row=0, column=0, padx=10, sticky=W)
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=('sans serif', 10, 'bold'), width=17, state='readonly',
                                 cursor='hand2')
        dep_combo['values'] = ('Select Department', 'IT', "Management", "Financial", "Administration", 'other')
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, pady=10, padx=2, sticky=W)

        # Basic Salary

        salary_label = Label(current_course_frame, text='Basic Salary', font=("sans serif", 10, 'bold'))
        salary_label.grid(row=0, column=2, padx=10, sticky=W)
        salary_combo = ttk.Combobox(current_course_frame, textvariable= self.var_Bsalary,  font=('sans serif', 10, 'bold'), width=17, state='readonly',
                                 cursor='hand2')
        salary_combo['values'] = ('0', '<10,000', '10,000-50,000', '50,000-2 lacs', '2 lacs-10 lacs', '>10 lacs')
        salary_combo.current(0)
        salary_combo.grid(row=0, column=3, pady=10, padx=2, sticky=W)

        # Shift

        shift_label = Label(current_course_frame, text='Shift', font=("sans serif", 10, 'bold'))
        shift_label.grid(row=2, column=0, padx=10, sticky=W)
        shift_combo = ttk.Combobox(current_course_frame, textvariable=self.var_shift, font=('sans serif', 10, 'bold'), width=17, state='readonly',
                                 cursor='hand2')
        shift_combo['values'] = ('Select', 'Morning', 'Afternoon', 'Night')
        shift_combo.current(0)
        shift_combo.grid(row=2, column=1, pady=10, padx=2, sticky=W)

        # Job role

        job_label = Label(current_course_frame, text='Job Role', font=("sans serif", 10, 'bold'))
        job_label.grid(row=2, column=2, padx=10, sticky=W)
        self.job = ttk.Entry(current_course_frame, textvariable=self.var_Job, font=('Sans serif', 10, 'bold'))
        self.job.grid(row=2, column=3, padx=2, pady=10, sticky=W)

        # Employee branch

        employee_frame = LabelFrame(left_frame, bd=5, relief=RIDGE, text='Employee Personal Details',
                                          font=('sans serif', 10, 'bold'))
        employee_frame.place(x=0, y=300, width=670, height=300)

        # Employee ID

        employee_ID_label = Label(employee_frame, text='Employee ID:', font=('sans serif', 10, 'bold'))
        employee_ID_label.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        employee_ID_entry = ttk.Entry(employee_frame, textvariable=self.var_EId, width=20, font=('sans serif', 10, 'bold'))
        employee_ID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Employee Name

        employee_name_label = Label(employee_frame, text='Employee Name:', font=('sans serif', 10, 'bold'))
        employee_name_label.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        employee_name_entry = ttk.Entry(employee_frame, textvariable=self.var_name, width=25, font=('sans serif', 10, 'bold'))
        employee_name_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Address

        Adress_label = Label(employee_frame, text='Address', font=('sans serif', 10, 'bold'))
        Adress_label.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        Adress_entry = ttk.Entry(employee_frame, width=25, textvariable=self.var_addr, font=('sans serif', 10, 'bold'))
        Adress_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        Gender_label = Label(employee_frame, text='Gender', font=('sans serif', 10, 'bold'))
        Gender_label.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        # Gender_entry = ttk.Entry(employee_frame, width=20, font=('sans serif', 10, 'bold'))
        Gender_combo = ttk.Combobox(employee_frame, textvariable=self.var_gender, font=('sans serif', 10, 'bold'), width=18, state='readonly',
                                   cursor='hand2')
        Gender_combo['values'] = ('Select', 'Male', 'Female', 'Other')
        Gender_combo.current(0)
        Gender_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Date Of Birth

        YOJ_label = Label(employee_frame, text='DOB', font=('sans serif', 10, 'bold'))
        YOJ_label.grid(row=2, column=0, padx=5, pady=10, sticky=W)
        YOJ_entry = ttk.Entry(employee_frame, width=20, textvariable=self.var_dob, font=('sans serif', 10, 'bold'))
        YOJ_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Email

        email_ID_label = Label(employee_frame, text='Email Id:', font=('sans serif', 10, 'bold'))
        email_ID_label.grid(row=2, column=2, padx=5, pady=10, sticky=W)
        email_ID_entry = ttk.Entry(employee_frame, textvariable=self.var_email, width=25, font=('sans serif', 10, 'bold'))
        email_ID_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Mobile number

        mob_label = Label(employee_frame, text='Mobile Number', font=('sans serif', 10, 'bold'))
        mob_label.grid(row=3, column=0, padx=5, pady=10, sticky=W)
        mob_entry = ttk.Entry(employee_frame,textvariable=self.var_mob, width=20, font=('sans serif', 10, 'bold'))
        mob_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # HOD

        hod_label = Label(employee_frame, text='Head of Department', font=('sans serif', 10, 'bold'))
        hod_label.grid(row=3, column=2, padx=5, pady=10, sticky=W)
        hod_entry = ttk.Entry(employee_frame, textvariable=self.var_hod, width=25, font=('sans serif', 10, 'bold'))
        hod_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


        # Button

        btn_frame = LabelFrame(employee_frame, bd=2, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=200, width=660, height=35)

        save_btn = Button(btn_frame, text='Save', command= self.add_data, width=20, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue')
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text='Update', width=20, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.update_data)
        update_btn.grid(row=0, column=1)

        delete_btn = Button(btn_frame, text='Delete', width=20, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.delete_data)
        delete_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text='Reset', width=20, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.reset_data)
        reset_btn.grid(row=0, column=3)

        btn_frame2 = LabelFrame(employee_frame, bd=1, relief=RIDGE, bg='white')
        btn_frame2.place(x=0, y=235, width=660, height=35)
        #
        take_photo_sample_btn = Button(btn_frame2, width=41, text='Take Photo Sample', font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.generate_dataset)
        take_photo_sample_btn.grid(row=1, column=2)

        # Right Label Frame

        right_frame = LabelFrame(main_frame, bd=5, relief=RIDGE, text='Employee Details', font=("Sans serif", 15, 'bold'))
        right_frame.place(x=700, y=10, width=680, height=630)

        # Image at the right frame!

        img_right = Image.open("Images//right_frame.png")
        img_right.resize((660, 180), Image.Resampling.LANCZOS)
        self.img_right = ImageTk.PhotoImage(img_right)
        right_lbl = Label(right_frame, image=self.img_right)
        right_lbl.place(x=0, y=0, width=660, height=188)

        # Table Frame..

        table_frame = LabelFrame(right_frame, bd=5, relief=RIDGE, text='Employee Personal Details',
                                          font=('sans serif', 10, 'bold'))
        table_frame.place(x=0, y=200, width=670, height=400)

        # Scroll bar

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL, cursor='hand2')
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL, cursor='hand2')

        self.Employee_table = ttk.Treeview(table_frame, columns=('name', 'bas_salary', 'shift', 'job_role',
                                                                 'emp_id', 'dep', 'gender', 'addr', 'dob', 'email',
                                                                 'mob', 'hod'), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)

        # Heading of the employee

        self.Employee_table.heading('name', text="Employee Name")
        self.Employee_table.heading('bas_salary', text="Basic Salary")
        self.Employee_table.heading('shift', text="Shift")
        self.Employee_table.heading('job_role', text="Job Role")
        self.Employee_table.heading('emp_id', text="Employee Id")
        self.Employee_table.heading('dep', text="Department")
        self.Employee_table.heading('gender', text="Gender")
        self.Employee_table.heading('addr', text="Address")
        self.Employee_table.heading('dob', text="Date Of Birth")
        self.Employee_table.heading('email', text="Email")
        self.Employee_table.heading('mob', text="Mobile Number")
        self.Employee_table.heading('hod', text="Head Of Department")
        self.Employee_table["show"] = 'headings'

        self.Employee_table.pack(fill=BOTH, expand=1)

        self.Employee_table.column('name', width=100)
        self.Employee_table.column('bas_salary', width=100)
        self.Employee_table.column('shift', width=100)
        self.Employee_table.column('job_role', width=100)
        self.Employee_table.column('emp_id', width=100)
        self.Employee_table.column('dep', width=100)
        self.Employee_table.column('gender', width=100)
        self.Employee_table.column('addr', width=100)
        self.Employee_table.column('dob', width=100)
        self.Employee_table.column('email', width=100)
        self.Employee_table.column('mob', width=100)
        self.Employee_table.column('hod', width=100)

        self.Employee_table.pack(fill=BOTH, expand=1)
        self.Employee_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # Function for entry in database

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_EId.get() == "" or self.var_name.get() == "" or \
                self.var_gender.get() == 'Select' or self.var_email.get() == "":
            messagebox.showerror("Error!", "All Fields are Required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host='localhost', user='root', password = 'Ssrv@005', database='swym')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into swym.employee_data values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                  (self.var_name.get(), self.var_Bsalary.get(), self.var_shift.get(), self.var_Job.get(),
                                   self.var_EId.get(), self.var_dep.get(), self.var_gender.get(), self.var_addr.get(),
                                   self.var_dob.get(), self.var_email.get(), self.var_mob.get(), self.var_hod.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "{} Registered".format(self.var_name.get()), parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", "Due to{}".format(str(e)), parent=self.root)

        # ########## Fetch data################

    def fetch_data(self):

        conn = mysql.connector.connect(host="localhost", user="root", password="Ssrv@005", database="swym")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from swym.employee_data")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.Employee_table.delete(*self.Employee_table.get_children())
            for i in data:
                self.Employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        cursor_focus = self.Employee_table.focus()
        content = self.Employee_table.item(cursor_focus)
        data = content["values"]

        self.var_name.set(data[0]),
        self.var_Bsalary.set(data[1]),
        self.var_shift.set(data[2]),
        self.var_Job.set(data[3]),
        self.var_EId.set(data[4]),
        self.var_dep.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_addr.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_mob.set(data[10]),
        self.var_hod.set(data[11]),

    # Update Button

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_EId.get() == "" or self.var_name.get() == "" or \
                self.var_gender.get() == 'Select' or self.var_email.get() == "":
            messagebox.showerror("Error!", "All Fields are Required!", parent=self.root)

        else:
            try:
                Update = messagebox.askyesno("Update!", "Do you want to update this statement details", parent = self.root)
                if Update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Ssrv@005", database="swym")
                    my_cursor = conn.cursor()

                    query1 = "UPDATE swym.employee_data SET name=%s WHERE EId = %s"
                    data1 = (self.var_name.get(), self.var_EId.get())
                    my_cursor.execute(query1, data1)

                    query2 = "UPDATE swym.employee_data SET bsalary=%s WHERE EId = %s"
                    data2 = (self.var_Bsalary.get(), self.var_EId.get())
                    my_cursor.execute(query2, data2)

                    query3 = "UPDATE swym.employee_data SET shift=%s WHERE EId = %s"
                    data3 = (self.var_shift.get(), self.var_EId.get())
                    my_cursor.execute(query3, data3)

                    query4 = "UPDATE swym.employee_data SET job=%s WHERE EId = %s"
                    data4 = (self.var_Job.get(), self.var_EId.get())
                    my_cursor.execute(query4, data4)

                    query5 = "UPDATE swym.employee_data SET Dep=%s WHERE EId = %s"
                    data5 = (self.var_dep.get(), self.var_EId.get())
                    my_cursor.execute(query5, data5)

                    data6 = (self.var_addr.get(), self.var_EId.get())
                    query6 = "UPDATE swym.employee_data SET addr=%s WHERE EId = %s"
                    my_cursor.execute(query6, data6)

                    query7 = "UPDATE swym.employee_data SET gender=%s WHERE EId = %s"
                    data7 = (self.var_gender.get(), self.var_EId.get())
                    my_cursor.execute(query7, data7)

                    query8 = "UPDATE swym.employee_data SET dob=%s WHERE EId = %s"
                    data8 = (self.var_dob.get(), self.var_EId.get())
                    my_cursor.execute(query8, data8)

                    query9 = "UPDATE swym.employee_data SET email=%s WHERE EId = %s"
                    data9 = (self.var_email.get(), self.var_EId.get())
                    my_cursor.execute(query9, data9)

                    query10 = "UPDATE swym.employee_data SET mob=%s WHERE EId = %s"
                    data10 = (self.var_mob.get(), self.var_EId.get())
                    my_cursor.execute(query10, data10)

                    query11 = "UPDATE swym.employee_data SET hod=%s WHERE EId = %s"
                    data11 = (self.var_hod.get(), self.var_EId.get())
                    my_cursor.execute(query11, data11)

                    query12 = "UPDATE swym.employee_data SET EId=%s WHERE EId = %s"
                    data12 = (self.var_EId.get(), self.var_EId.get())
                    my_cursor.execute(query12, data12)
                    """
                    # query = "UPDATE swym.employee_data SET name=%s, bsalary=%s, shift=%s, job=%s, Dep=%s, gender=%s, addr=%s, dob=%s, email=%s, mob=%s, hod=%s  where EId=%s" 
                    # data = (self.var_name.get(), self.var_Bsalary, self.var_shift, self.var_Job, self.var_dep, self.var_gender, self.var_addr, self.var_dob, self.var_email, self.var_mob, self.var_hod, self.var_EId.get())
                    """

                else:
                    if not Update:
                        return

                messagebox.showinfo("Success!", "{} details Updated Successfully".format(self.var_name.get()))
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as e:
                messagebox.showerror("Error", "Error Due to:{}".format(str(e)))

            # Delete Function
    def delete_data(self):
        if self.var_EId.get() == "":
            messagebox.showerror("Error", "Please Enter the Employee ID", parent=self.root)

        else:
            try:
                delete =messagebox.askyesno("Employee Delete?", "Do you want to Delete?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Ssrv@005", database="swym")
                    my_cursor = conn.cursor()
                    sql = "delete from swym.employee_data where EId = %s"
                    val = (self.var_EId.get(), )
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted", "Successfully deleted Employee", parent=self.root)

            except Exception as e:
                messagebox.showerror("Error", "Error Due to:{}".format(str(e)))

        # RESET

    def reset_data(self):
        self.var_name.set(""),
        self.var_Bsalary.set("0"),
        self.var_shift.set("Select"),
        self.var_Job.set(""),
        self.var_EId.set(""),
        self.var_dep.set("Select Department"),
        self.var_gender.set("Select"),
        self.var_addr.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_mob.set(""),
        self.var_hod.set(""),

#  ++++++++++++++++++++GENERATE DATA SET######################

    def generate_dataset(self):

        if self.var_dep.get() == "Select Department" or self.var_EId.get() == "" or self.var_name.get() == "" or \
                self.var_gender.get() == 'Select' or self.var_email.get() == "":
            messagebox.showerror("Error!", "All Fields are Required!", parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Ssrv@005", database="swym")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from swym.employee_data")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id += 1

                query1 = "UPDATE swym.employee_data SET name=%s WHERE EId = %s"
                data1 = (self.var_name.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query1, data1)

                query2 = "UPDATE swym.employee_data SET bsalary=%s WHERE EId = %s"
                data2 = (self.var_Bsalary.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query2, data2)

                query3 = "UPDATE swym.employee_data SET shift=%s WHERE EId = %s"
                data3 = (self.var_shift.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query3, data3)

                query4 = "UPDATE swym.employee_data SET job=%s WHERE EId = %s"
                data4 = (self.var_Job.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query4, data4)

                query5 = "UPDATE swym.employee_data SET Dep=%s WHERE EId = %s"
                data5 = (self.var_dep.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query5, data5)

                data6 = (self.var_addr.get(), self.var_EId.get()==id+1)
                query6 = "UPDATE swym.employee_data SET addr=%s WHERE EId = %s"
                my_cursor.execute(query6, data6)

                query7 = "UPDATE swym.employee_data SET gender=%s WHERE EId = %s"
                data7 = (self.var_gender.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query7, data7)

                query8 = "UPDATE swym.employee_data SET dob=%s WHERE EId = %s"
                data8 = (self.var_dob.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query8, data8)

                query9 = "UPDATE swym.employee_data SET email=%s WHERE EId = %s"
                data9 = (self.var_email.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query9, data9)

                query10 = "UPDATE swym.employee_data SET mob=%s WHERE EId = %s"
                data10 = (self.var_mob.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query10, data10)

                query11 = "UPDATE swym.employee_data SET hod=%s WHERE EId = %s"
                data11 = (self.var_hod.get(), self.var_EId.get()==id+1)
                my_cursor.execute(query11, data11)

                query12 = "UPDATE swym.employee_data SET EId=%s WHERE EId = %s"
                data12 = (self.var_EId.get(), self.var_EId.get())
                my_cursor.execute(query12, data12)

                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ++++++++++++++++LOAD  predefined data on face from open cv

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling Factor = 1.3
                    # Minimum Neighbor = 5
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (800, 800))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data//user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)
                        time.sleep(0.1)
                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data Set Completed")
            except Exception as e:
                messagebox.showerror("Error", "Error Due to:{}".format(str(e)))


if __name__ == '__main__':
    root = Tk()
    obj = Employee(root)
    root.mainloop()