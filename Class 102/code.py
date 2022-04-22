from ast import While
from tkinter import Frame, image_names
from tracemalloc import start
import cv2
from cv2 import VideoCapture
import random 
import time

startTime=time.time()

def takeSnapshot():
    number= random.randint(0,100)
    VideoCaptureObject = cv2.VideoCapture(0)
    Result = True
    while(Result):
        ret,Frame = VideoCaptureObject.read()
        imagename = "img" + str(number) + ".png"
        cv2.imwrite(imagename,Frame)
        startTime = time.time()
        Result = False
    return imagename
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
takeSnapshot()