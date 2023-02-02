from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import cv2
import os.path
import numpy as np


def train_classifier():
    data_dir = ("data")
    path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert("L")   # GRAY SCALE IMAGE
        ImageNp = np.array(img, 'uint8')   # Conversion in grid system
        id = int(os.path.split(image)[1].split('.')[1])
        faces.append(ImageNp)
        ids.append(id)
        cv2.imshow("Training", ImageNp)
        var = cv2.waitKey(1) == 13
    ids = np.array(ids)

    # Train classifier

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("Result", "Training Dataset completed")


