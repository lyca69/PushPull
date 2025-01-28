from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PIL import Image, ImageEnhance #Library Pillow untuk manipulasi gambar

from display import Ui_Form
import numpy as np


class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #Display gambar menggunakan Label yang dihide/dibuat tidak keliatan
        self.ui.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #Trigger button
        self.ui.pushButton.clicked.connect(self.selectImage)
        self.ui.pushButton_2.clicked.connect(self.selectColor)

        #Slider Contrast
        self.ui.horizontalSlider.setRange(0,200)
        self.ui.horizontalSlider.setValue(100)#Kondisi awal di 100% / Normal
        self.ui.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.ui.horizontalSlider.setTickInterval(10)
        self.ui.horizontalSlider.valueChanged.connect(self.apply_adjustment)

        #Slider Brightness
        self.ui.horizontalSlider_2.setRange(-100,100)
        self.ui.horizontalSlider_2.setValue(0)
        self.ui.horizontalSlider_2.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.ui.horizontalSlider_2.setTickInterval(10)
        self.ui.horizontalSlider_2.valueChanged.connect(self.apply_adjustment)

        self.image=None
        self.pil_image=None
        self.adjusted_image=None
        self.color=QColor(255,255,255)

    def selectImage(self):
        file,_=QFileDialog.getOpenFileName(self,'Images(*.png *.jpg *.jpeg)')
        if file:
            self.pil_image=Image.open(file)
            self.adjusted_image=self.pil_image.copy()
            self.displayImage()
    
    def displayImage(self):
         if self.adjusted_image:
            qimage = self.pil_to_qimage(self.adjusted_image)
            pixmap = QPixmap(qimage)
            self.ui.label_2.setPixmap(pixmap)

    def pil_to_qimage(self,pil_image):
        #Convert dari Pillow ke QImage
        pil_image=pil_image.convert("RGBA") #Mengkonversi image menjadi RGBA
        data=pil_image.tobytes("raw","RGBA")
        qimage=QImage(data, pil_image.width, pil_image.height, QImage.Format.Format_RGBA8888)
        return qimage

    def selectColor(self):
        color=QColorDialog.getColor(self.color,self)
        if color.isValid():
            self.color=color
            self.apply_color_filter()

    def apply_color_filter(self):
        if self.adjusted_image:
            color_matrix=np.array([
                [1, 0, 0, self.color.red()],
                [0, 1, 0, self.color.green()],
                [0, 0, 1, self.color.blue()],
                [0, 0, 0, 1]
            ])

        #Convert Image ke array agar mudah dimanipulasi
        img_array = np.array(self.adjusted_image)
        img_array = np.dot(img_array[...,:3], color_matrix[:3,:3].T) + color_matrix[:3,3]
        img_array = np.clip(img_array, 0, 255).astype(np.uint8)

        # Konversi Array ke Image kemabali
        self.adjusted_image = Image.fromarray(img_array)
        self.displayImage()

    def apply_adjustment(self):
        if self.pil_image:
            contrast=self.ui.horizontalSlider.value()/100
            brightness=self.ui.horizontalSlider_2.value()

            #Apply Contrast adjustment using Pillow
            enhancer=ImageEnhance.Contrast(self.pil_image)
            self.adjusted_image=enhancer.enhance(contrast)        

            #Apply Brightness adjustment using Pillow
            enhancer=ImageEnhance.Brightness(self.adjusted_image)
            self.adjusted_image=enhancer.enhance(1+brightness/100)

            self.displayImage()