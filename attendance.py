import os
import time
import employee
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
import time
import csv
from tkinter import filedialog

mydata = []


class Attendance:

    def __init__(self, root):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title("Employee Section ")
        self.root.wm_iconbitmap("icon_.ico")


        # ################### VARIABLES ##################

        self.var_Eid = StringVar()
        self.var_attendance = StringVar()
        self.var_date = StringVar()
        self.var_dep = StringVar()
        self.var_time = StringVar()
        self.var_name = StringVar()

        # BG PICTURE

        img = Image.open("Images//UI_backimage.png")
        img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        # ImageTk module contains support to create and modify Tkinter BitmapImage and PhotoImage objects from PIL image
        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, relwidth=1, relheight=1)

        # Label

        fras = Label(self.root, text='Attendance', font=('Blackletter', 25, 'bold'),
                     bg='#0C090A', fg='white')
        fras.place(x=0, y=10, height=50, width=1550)

        # Frame

        main_frame = Frame(bg_img, bd=2, bg='white')
        main_frame.place(x=75, y=100, width=1400, height=650)

        # Left Label Frame

        left_frame = LabelFrame(main_frame, bd=5, relief=RIDGE, text='Attendance Details ', font=("Sans serif", 15, 'bold'), bg='white')
        left_frame.place(x=10, y=10, width=680, height=630)

        # IMAGE On Left frame

        img_left = Image.open("Images//attendace.png")
        img_left.resize((660, 180), Image.Resampling.LANCZOS)
        self.img_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.img_left, bg='white')
        f_lbl.place(x=0, y=0, width=660, height=200)

        # Employee branch

        employee_frame = LabelFrame(left_frame, bd=5, relief=RIDGE, text='Employee Personal Details',
                                    font=('sans serif', 10, 'bold'),bg='white')
        employee_frame.place(x=0, y=200, width=670, height=400)

        # Attendance
        Attendance_label = Label(employee_frame, text='Attendance:', font=('sans serif', 10, 'bold'))
        Attendance_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        Attendance_combo = ttk.Combobox(employee_frame, font=('sans serif', 10, 'bold'),
                                        width=22, state='readonly', textvariable= self.var_attendance,
                                        cursor='hand2')
        Attendance_combo['values'] = ('Status', "Present", "Absent")
        Attendance_combo.current(0)
        Attendance_combo.grid(row=0, column=1, pady=5, padx=15, sticky=W)

        # Employee_ID

        Employee_ID_label = Label(employee_frame, text='Employee ID:', font=('sans serif', 10, 'bold'))
        Employee_ID_label.grid(row=0, column=2, padx=10, pady=10, sticky=W)
        Employee_ID_entry = ttk.Entry(employee_frame, width=25, font=('sans serif', 10, 'bold'), textvariable=self.var_Eid)
        Employee_ID_entry.grid(row=0, column=3, padx=15, pady=5, sticky=W)

        # Date

        date_label = Label(employee_frame, text='Date:', font=('sans serif', 10, 'bold'))
        date_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        date_entry = ttk.Entry(employee_frame, width=20, font=('sans serif', 10, 'bold'), textvariable=self.var_date)
        date_entry.grid(row=1, column=1, padx=15, pady=5, sticky=W)

        # Department Name

        dep_label = Label(employee_frame, text='Department', font=("sans serif", 10, 'bold'))
        dep_label.grid(row=1, column=2, padx=10, sticky=W)
        dep_combo = ttk.Combobox(employee_frame, font=('sans serif', 10, 'bold'),
                                 width=22, state='readonly', textvariable=self.var_dep,
                                 cursor='hand2')
        dep_combo['values'] = ('Select Department', 'IT', "Management", "Financial", "Administration", 'other')
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, pady=5, padx=15, sticky=W)

        # Time

        Time_label = Label(employee_frame, text='Time:', font=('sans serif', 10, 'bold'))
        Time_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        Time_entry = ttk.Entry(employee_frame, width=20, font=('sans serif', 10, 'bold'), textvariable=self.var_time)
        Time_entry.grid(row=2, column=1, padx=15, pady=5, sticky=W)

        # Employee Name

        employee_name_label = Label(employee_frame, text='Employee Name:', font=('sans serif', 10, 'bold'))
        employee_name_label.grid(row=2, column=2, padx=10, pady=10, sticky=W)
        employee_name_entry = ttk.Entry(employee_frame, width=25, font=('sans serif', 10, 'bold'), textvariable=self.var_name)
        employee_name_entry.grid(row=2, column=3, padx=15, sticky=W)

        # Button

        btn_frame = LabelFrame(employee_frame, bd=0, relief=RIDGE, bg='white')
        btn_frame.place(x=0, y=175, width=660, height=150)

        Import_btn = Button(btn_frame, text='Import', width=20, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.import_CSV)
        Import_btn.grid(row=0, column=0, padx=80, pady=20)

        Export_btn = Button(btn_frame, text='Export', width=20, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.export_CSV)
        Export_btn.grid(row=0, column=3, padx=80, pady=20)

        reset_btn = Button(btn_frame, text='Reset', width=30, font=('sans serif', 10, 'bold'), bg='blue', fg='white',
                          activeforeground='white', activebackground='blue', command=self.reset_data)
        reset_btn.grid(row=1, column=0, padx=40, pady=10)

        # Right Label Frame

        right_frame = LabelFrame(main_frame, bd=5, relief=RIDGE, text='Employee Attendance list',
                                 font=("Sans serif", 15, 'bold'), bg='white')
        right_frame.place(x=700, y=10, width=680, height=630)

        # Table Frame

        table_frame = LabelFrame(right_frame, bd=5, relief=RIDGE,
                                  font=('sans serif', 10, 'bold'))
        table_frame.place(x=0, y=5, width=670, height=595)

        # SCROLL BAR

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL, cursor='hand2')
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL, cursor='hand2')

        self.Attendance_Report_Table = ttk.Treeview(table_frame, columns=("Employee_id", "name", "department", "Time", "Date", "Attendance"), xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Attendance_Report_Table.xview)
        scroll_y.config(command=self.Attendance_Report_Table.yview)

        # Heading of the employee

        self.Attendance_Report_Table.heading('Employee_id', text="Employee ID")
        self.Attendance_Report_Table.heading('name', text="Name")
        self.Attendance_Report_Table.heading('department', text="Department")
        self.Attendance_Report_Table.heading('Time', text="Time")
        self.Attendance_Report_Table.heading("Date", text="Date")
        self.Attendance_Report_Table.heading('Attendance', text="Attendance")
        self.Attendance_Report_Table["show"] = 'headings'

        self.Attendance_Report_Table.column('Employee_id', width =100)
        self.Attendance_Report_Table.column('name', width =100)
        self.Attendance_Report_Table.column('department', width =100)
        self.Attendance_Report_Table.column('Time', width =100)
        self.Attendance_Report_Table.column("Date", width =100)
        self.Attendance_Report_Table.column('Attendance', width =100)
        self.Attendance_Report_Table.pack(fill=BOTH, expand=1)

        self.Attendance_Report_Table.bind("<ButtonRelease>", self.get_cursor)

        # ####################  FETCH DATA ######################################

    def fetch_data(self, rows):

        self.Attendance_Report_Table.delete(*self.Attendance_Report_Table.get_children())
        for i in rows:
            self.Attendance_Report_Table.insert("", END, values=i)

    # Import CSV

    def import_CSV(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(file_name) as my_file:
            csvread = csv.reader(my_file, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    # EXPORT CSV

    def export_CSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data found", parent = self.root)
                return False
            else:
                file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
                with open(file_name, mode='w', newline="") as myfile:
                    exp_write = csv.writer(myfile, delimiter=",")
                    for i in mydata:
                        exp_write.writerow(i)
                    messagebox.showinfo("Success!","Attendance exported.")
        except Exception as e:
            messagebox.showerror("Error!", "Due to {}".format(str(e)), parent = self.root)

    # GET CURSOR

    def get_cursor(self, event = ""):

        cursor_row = self.Attendance_Report_Table.focus()
        content = self.Attendance_Report_Table.item(cursor_row)
        row = content['values']
        self.var_Eid.set(row[0])
        self.var_name.set(row[1])
        self.var_time.set(row[3])
        self.var_dep.set(row[2])
        self.var_date.set(row[4])
        self.var_attendance.set(row[5])

    # RESET............

    def reset_data(self):
        self.var_attendance.set("Status")
        self.var_Eid.set("")
        self.var_date.set("")
        self.var_dep.set("Select Department")
        self.var_time.set("")
        self.var_name.set("")


if __name__ == '__main__':
    root = Tk()
    ob4 = Attendance(root)
    root.mainloop()