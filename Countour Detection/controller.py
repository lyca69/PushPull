from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
# from PIL import Image, ImageEnhance #Library Pillow untuk manipulasi gambar
from PIL import Image
import cv2

from display import Ui_Form
import numpy as np


class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #Display gambar menggunakan Label yang dihide/dibuat tidak keliatan
        self.ui.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Trigger for Button
        self.ui.pushButton.clicked.connect(self.originalmage) #Original Image
        self.ui.pushButton_2.clicked.connect(self.grayImage) #Grayscale
        self.ui.pushButton_3.clicked.connect(self.AdaptiveThreshold) #Adaptive Threshold
        self.ui.pushButton_4.clicked.connect(self.CannyEdge) #Canny Edge
        self.ui.pushButton_5.clicked.connect(self.processedImage) #Processed Image(Contour in original image)
        self.ui.pushButton_6.clicked.connect(self.selectImage)

    def pil_to_qimage(self,pil_image):#Convert dari Pillow ke QImage
        pil_image=pil_image.convert("RGBA")
        data=pil_image.tobytes("raw","RGBA")
        qimage=QImage(data,pil_image.width,pil_image.height,QImage.Format.Format_RGBA8888)
        return qimage
                    
    def selectImage(self):
        file,_=QFileDialog.getOpenFileName(self,'Images(*.png *.img *.jpeg)')
        if file:
            self.image=Image.open(file)
            self.adjusted_image=self.image.copy()
            self.displayImage()
    
    def displayImage(self):
        if self.adjusted_image:
            qimage=self.pil_to_qimage(self.adjusted_image)
            pixmap=QPixmap(qimage)
            self.ui.label.setPixmap(pixmap)
    
    def originalmage(self):
        if hasattr(self,'image'):#Cek jika gambar sudah diunggah
            self.original_image=self.image.copy()
            self.adjusted_image=self.original_image
            self.displayImage()    

    def grayImage(self):
        if hasattr(self,'image'):#Cek jika gambar sudah diunggah
            #Konversi dari PIL ke OpenCV
            open_cv_image=np.array(self.image)
            open_cv_image=cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR)

            gray_image=cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)

            self.adjusted_image=Image.fromarray(gray_image)
            self.displayImage()
        else :
            QMessageBox.warning(self,"Warning", "Please select an image first!")

    def AdaptiveThreshold(self):
        if hasattr(self,'image'):#Cek jika gambar sudah diunggah
            open_cv_image=np.array(self.image)
            open_cv_image=cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR)

            gray_image=cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)
            adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
            self.adjusted_image=Image.fromarray(adaptive_threshold)
            self.displayImage()
        else:
            QMessageBox.warning(self,"Warning", "Please select an image first!")
     
    def CannyEdge(self):
        if hasattr(self,'image'):#Cek jika gambar sudah diunggah
            open_cv_image=np.array(self.image)
            open_cv_image=cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR)

            gray_image=cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)

            canny_edge=cv2.Canny(gray_image,50,150)

            self.adjusted_image=Image.fromarray(canny_edge)
            self.displayImage()
        else:
            QMessageBox.warning(self,"Warning", "Please select an image first!")

    def processedImage(self): 
        # if hasattr(self,'image'):#Cek jika gambar sudah diunggah
        #     open_cv_image=np.array(self.image)
        #     open_cv_image-=cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR)

        #     gray_image=cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)
        #     adaptive_threshold=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
        #     contours, hierarchy=cv2.findContours(adaptive_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #     contours=[c for c in contours if cv2.contourArea(c) > 100]

        #     drawcontours=cv2.drawContours(open_cv_image,contours,-1,(0,255,0),1)
        #     self.adjusted_image=Image.fromarray(drawcontours)
        #     self.displayImage()
        # else:
        #     QMessageBox.warning(self,"Warning","Please select an image first!")

        if hasattr(self,'image'):#Cek jika gambar sudah diunggah
            open_cv_image=np.array(self.image)
            open_cv_image=cv2.cvtColor(open_cv_image,cv2.COLOR_RGB2BGR)

            gray_image=cv2.cvtColor(open_cv_image,cv2.COLOR_BGR2GRAY)
            adaptive_threshold=cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
            canny_edge=cv2.Canny(gray_image,50,150) #Mencari tepi dengan patokan gambar grayscale

            contours,_=cv2.findContours(adaptive_threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            contours=[c for c in contours if cv2.contourArea(c) > 100]
            print("Number of contours : "+str(len(contours)))

            drawcontours=cv2.drawContours(open_cv_image,contours,-1,(0,255,0),1)


            kernel=np.ones((3,3), np.uint8)
            processed_img=cv2.erode(canny_edge,kernel,iterations=1)
            processed_img=cv2.dilate(processed_img,kernel,iterations=1)

            self.adjusted_image=Image.fromarray(drawcontours)
            self.displayImage()
        else:
            QMessageBox.warning(self,"Warning","Please select an image first!")
        