import time
import employee
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
from datetime import datetime


def mark_attendance(name, Employid, Dep):
    with open("Attendance.csv", 'r+', newline="\n") as f:
        myData_list = f.readlines()
        name_list = []
        for line in myData_list:
            entry = line.split(",")  # CSV file comma seperated values
            name_list.append(entry[0])
            now = datetime.now()
            d1 = now.strftime("%d//%m//%Y")
            dtString = now.strftime("%H:%M:%S")
        if ((name not in name_list) and (Dep not in name_list) and (Employid not in name_list) and (d1 not in name_list) and (d1 not in name_list)):
            now = datetime.now()
            d1 = now.strftime("%d//%m//%Y")
            dtString = now.strftime("%H:%M:%S")
            f.writelines("\n{}, {}, {},{}, {}, Present".format(Employid, name, Dep, dtString, d1))


def face_recog():

    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        cord = []
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
            # To draw a rectangle over a face
            id, predict = clf.predict(gray_image[y:y+h, x:x+w])
            # Training with the help of histogram
            confidence = int((100*(1-predict/300)))
            # Lower confidence are better because it means 2 histogram were closer

            conn = mysql.connector.connect(host="localhost", user="root", password="Ssrv@005", database="swym")
            my_cursor = conn.cursor()

            my_cursor.execute("select name from swym.employee_data where EId ="+str(id))
            nam = my_cursor.fetchone()
            nam = nam[0]

            my_cursor.execute("select Dep from swym.employee_data where EId =" + str(id))
            dep = my_cursor.fetchone()
            dep = dep[0]

            my_cursor.execute("select EId from swym.employee_data where EId =" + str(id))
            eid = my_cursor.fetchone()
            eid = eid[0]

            if confidence > 77:  # Percentage of accuracy
                cv2.putText(img, "Name-{}".format(nam), (x, y-55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),3)
                cv2.putText(img, "Emp Id-{}".format(eid), (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),3)
                cv2.putText(img, "Dep-{}".format(dep), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255),3)
                mark_attendance(nam, eid, dep)
            else:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "Unknown", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)

            cord = [x, y, w, y]
        return cord

    def recognize(img, clf, faceCascade):
        """
        :param img: Image which is received as Input
        :param clf: haar-cascade classifier
        :param faceCascade: Face detection which has been done using Haar-cascade classifier
        """
        cord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
        return img
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")
    video_cap = cv2.VideoCapture(0)
    # video_cap = cv2.VideoCapture(1)
    """ TO Set the different Camera which can be either web cam or external cam"""



    while True:
        ret, img = video_cap.read()
        img = recognize(img, clf, faceCascade)
        cv2.imshow("Welcome to the Face Recognition", img)

        if cv2.waitKey(1) == 13 or cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_cap.release()
    cv2.destroyAllWindows()


