import numpy
import os

#test fork (Pull Request)
#test fork (Pull Request 2)
#test fork (Pull Request 4)

imgcoba = face_recognition.load_image_file('peserta/Elon.jpg')
imgcoba = cv2.cvtColor(imgcoba, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Peserta/elon2.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)


cv2.imshow('Elon',imgcoba)
cv2.imshow('elon2',imgTest)
cv2.waitKey(0)
