# Code 1 :
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QImage, QPixmap, QColor
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QColorDialog

# class ImageColorCustomizer(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Picture Color Customization')
#         self.setGeometry(100, 100, 800, 600)

#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         self.select_image_button = QPushButton('Select Image', self)
#         self.select_image_button.clicked.connect(self.select_image)

#         self.select_color_button = QPushButton('Select Color', self)
#         self.select_color_button.clicked.connect(self.select_color)

#         self.layout = QVBoxLayout(self)
#         self.layout.addWidget(self.select_image_button)
#         self.layout.addWidget(self.select_color_button)
#         self.layout.addWidget(self.image_label)

#         self.image = None  # To store the loaded image
#         self.color = QColor(255, 255, 255)  # Default color (white)

#     def select_image(self):
#         file, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.bmp)')
#         if file:
#             self.image = QImage(file)
#             self.display_image()

#     def display_image(self):
#         if self.image:
#             pixmap = QPixmap(self.image)
#             self.image_label.setPixmap(pixmap)

#     def select_color(self):
#         color = QColorDialog.getColor(self.color, self)
#         if color.isValid():
#             self.color = color
#             self.apply_color_filter()

#     def apply_color_filter(self):
#         if self.image:
#             for x in range(self.image.width()):
#                 for y in range(self.image.height()):
#                     pixel_color = QColor(self.image.pixel(x, y))
#                     # Apply the chosen color by mixing the current pixel with the selected color
#                     blended_color = QColor(
#                         min(pixel_color.red() + self.color.red(), 255),
#                         min(pixel_color.green() + self.color.green(), 255),
#                         min(pixel_color.blue() + self.color.blue(), 255)
#                     )
#                     self.image.setPixel(x, y, blended_color.rgba())
#             self.display_image()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ImageColorCustomizer()
#     window.show()
#     sys.exit(app.exec())

#Code 2 :
# import sys
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QImage, QPixmap, QColor
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QColorDialog, QSlider, QHBoxLayout, QGroupBox, QFormLayout

# class ImageColorCustomizer(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Picture Color Customization')
#         self.setGeometry(100, 100, 800, 600)

#         # Create label to display image
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         # Create buttons for image and color selection
#         self.select_image_button = QPushButton('Select Image', self)
#         self.select_image_button.clicked.connect(self.select_image)

#         self.select_color_button = QPushButton('Select Color', self)
#         self.select_color_button.clicked.connect(self.select_color)

#         # Create sliders for contrast and brightness adjustment
#         self.contrast_slider = QSlider(Qt.Orientation.Horizontal, self)
#         self.contrast_slider.setRange(0, 200)
#         self.contrast_slider.setValue(100)
#         self.contrast_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
#         self.contrast_slider.setTickInterval(10)
#         self.contrast_slider.valueChanged.connect(self.apply_adjustments)

#         self.brightness_slider = QSlider(Qt.Orientation.Horizontal, self)
#         self.brightness_slider.setRange(-100, 100)
#         self.brightness_slider.setValue(0)
#         self.brightness_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
#         self.brightness_slider.setTickInterval(10)
#         self.brightness_slider.valueChanged.connect(self.apply_adjustments)

#         # Create layout for image adjustments
#         self.layout = QVBoxLayout(self)
#         self.layout.addWidget(self.select_image_button)
#         self.layout.addWidget(self.select_color_button)
#         self.layout.addWidget(self.image_label)

#         # Grouping sliders into a box
#         self.adjustments_group = QGroupBox('Adjustments', self)
#         form_layout = QFormLayout()
#         form_layout.addRow('Contrast', self.contrast_slider)
#         form_layout.addRow('Brightness', self.brightness_slider)
#         self.adjustments_group.setLayout(form_layout)
#         self.layout.addWidget(self.adjustments_group)

#         # Initialize variables
#         self.image = None
#         self.color = QColor(255, 255, 255)
#         self.adjusted_image = None

#     def select_image(self):
#         file, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.bmp)')
#         if file:
#             self.image = QImage(file)
#             self.adjusted_image = self.image.copy()
#             self.display_image()

#     def display_image(self):
#         if self.adjusted_image:
#             pixmap = QPixmap(self.adjusted_image)
#             self.image_label.setPixmap(pixmap)

#     def select_color(self):
#         color = QColorDialog.getColor(self.color, self)
#         if color.isValid():
#             self.color = color
#             self.apply_color_filter()

#     def apply_color_filter(self):
#         if self.adjusted_image:
#             for x in range(self.adjusted_image.width()):
#                 for y in range(self.adjusted_image.height()):
#                     pixel_color = QColor(self.adjusted_image.pixel(x, y))
#                     blended_color = QColor(
#                         min(pixel_color.red() + self.color.red(), 255),
#                         min(pixel_color.green() + self.color.green(), 255),
#                         min(pixel_color.blue() + self.color.blue(), 255)
#                     )
#                     self.adjusted_image.setPixel(x, y, blended_color.rgba())
#             self.display_image()

#     def apply_adjustments(self):
#         if self.image:
#             contrast = self.contrast_slider.value() / 100
#             brightness = self.brightness_slider.value()

#             # Copy the original image for adjustment
#             self.adjusted_image = self.image.copy()

#             for x in range(self.adjusted_image.width()):
#                 for y in range(self.adjusted_image.height()):
#                     pixel_color = QColor(self.adjusted_image.pixel(x, y))

#                     # Apply contrast adjustment
#                     red = int((pixel_color.red() - 128) * contrast + 128 + brightness)
#                     green = int((pixel_color.green() - 128) * contrast + 128 + brightness)
#                     blue = int((pixel_color.blue() - 128) * contrast + 128 + brightness)

#                     # Ensure color values are within valid range
#                     red = min(max(red, 0), 255)
#                     green = min(max(green, 0), 255)
#                     blue = min(max(blue, 0), 255)

#                     # Set the adjusted pixel back to the image
#                     self.adjusted_image.setPixel(x, y, QColor(red, green, blue).rgba())
#             self.display_image()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ImageColorCustomizer()
#     window.show()
#     sys.exit(app.exec())

#Code 3 :
# import sys
# from PIL import Image, ImageEnhance
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QImage, QPixmap
# from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QSlider, QGroupBox, QFormLayout

# class ImageColorCustomizer(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Picture Color Customization')
#         self.setGeometry(100, 100, 800, 600)

#         # Create label to display image
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

#         # Create buttons for image and color selection
#         self.select_image_button = QPushButton('Select Image', self)
#         self.select_image_button.clicked.connect(self.select_image)

#         # Create sliders for contrast and brightness adjustment
#         self.contrast_slider = QSlider(Qt.Orientation.Horizontal, self)
#         self.contrast_slider.setRange(0, 200)
#         self.contrast_slider.setValue(100)
#         self.contrast_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
#         self.contrast_slider.setTickInterval(10)
#         self.contrast_slider.valueChanged.connect(self.apply_adjustments)

#         self.brightness_slider = QSlider(Qt.Orientation.Horizontal, self)
#         self.brightness_slider.setRange(-100, 100)
#         self.brightness_slider.setValue(0)
#         self.brightness_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
#         self.brightness_slider.setTickInterval(10)
#         self.brightness_slider.valueChanged.connect(self.apply_adjustments)

#         # Create layout for image adjustments
#         self.layout = QVBoxLayout(self)
#         self.layout.addWidget(self.select_image_button)
#         self.layout.addWidget(self.image_label)

#         # Grouping sliders into a box
#         self.adjustments_group = QGroupBox('Adjustments', self)
#         form_layout = QFormLayout()
#         form_layout.addRow('Contrast', self.contrast_slider)
#         form_layout.addRow('Brightness', self.brightness_slider)
#         self.adjustments_group.setLayout(form_layout)
#         self.layout.addWidget(self.adjustments_group)

#         # Initialize variables
#         self.image = None
#         self.adjusted_image = None

#     def select_image(self):
#         file, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.bmp)')
#         if file:
#             self.image = Image.open(file)  # Open image using Pillow
#             self.adjusted_image = self.image.copy()
#             self.display_image()

#     def display_image(self):
#         if self.adjusted_image:
#             pixmap = QPixmap.fromImage(self.pil_image_to_qimage(self.adjusted_image))
#             self.image_label.setPixmap(pixmap)

#     def pil_image_to_qimage(self, pil_image):
#         """Convert Pillow image to QImage for display in PyQt"""
#         image_data = pil_image.tobytes("raw", "RGBA")
#         qimage = QImage(image_data, pil_image.width, pil_image.height, QImage.Format.Format_RGBA8888)
#         return qimage

#     def apply_adjustments(self):
#         if self.image:
#             contrast = self.contrast_slider.value() / 100
#             brightness = self.brightness_slider.value()

#             enhancer = ImageEnhance.Contrast(self.image)
#             self.adjusted_image = enhancer.enhance(contrast)

#             enhancer = ImageEnhance.Brightness(self.adjusted_image)
#             self.adjusted_image = enhancer.enhance(1 + brightness / 100)

#             self.display_image()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = ImageColorCustomizer()
#     window.show()
#     sys.exit(app.exec())


#Code 4 (2 yang dikasih Pillow ):
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QImage, QPixmap, QColor
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QColorDialog, QSlider, QGroupBox, QFormLayout
from PIL import Image, ImageEnhance
import numpy as np

class ImageColorCustomizer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Picture Color Customization')
        self.setGeometry(100, 100, 800, 600)

        # Create label to display image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create buttons for image and color selection
        self.select_image_button = QPushButton('Select Image', self)
        self.select_image_button.clicked.connect(self.select_image)

        self.select_color_button = QPushButton('Select Color', self)
        self.select_color_button.clicked.connect(self.select_color)

        # Create sliders for contrast and brightness adjustment
        self.contrast_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.contrast_slider.setRange(0, 200)
        self.contrast_slider.setValue(100)
        self.contrast_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.contrast_slider.setTickInterval(10)
        self.contrast_slider.valueChanged.connect(self.apply_adjustments)

        self.brightness_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.brightness_slider.setRange(-100, 100)
        self.brightness_slider.setValue(0)
        self.brightness_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.brightness_slider.setTickInterval(10)
        self.brightness_slider.valueChanged.connect(self.apply_adjustments)

        # Create layout for image adjustments
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.select_image_button)
        self.layout.addWidget(self.select_color_button)
        self.layout.addWidget(self.image_label)

        # Grouping sliders into a box
        self.adjustments_group = QGroupBox('Adjustments', self)
        form_layout = QFormLayout()
        form_layout.addRow('Contrast', self.contrast_slider)
        form_layout.addRow('Brightness', self.brightness_slider)
        self.adjustments_group.setLayout(form_layout)
        self.layout.addWidget(self.adjustments_group)

        # Initialize variables
        self.image = None
        self.pil_image = None
        self.adjusted_image = None
        self.color = QColor(255, 255, 255)

    def select_image(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.bmp)')
        if file:
            self.pil_image = Image.open(file)  # Open image using Pillow
            self.adjusted_image = self.pil_image.copy()
            self.display_image()

    def display_image(self):
        if self.adjusted_image:
            qimage = self.pil_to_qimage(self.adjusted_image)
            pixmap = QPixmap(qimage)
            self.image_label.setPixmap(pixmap)

    def pil_to_qimage(self, pil_image):
        """Convert Pillow image to QImage for PyQt"""
        pil_image = pil_image.convert("RGBA")  # Ensure image is in RGBA format
        data = pil_image.tobytes("raw", "RGBA")
        qimage = QImage(data, pil_image.width, pil_image.height, QImage.Format.Format_RGBA8888)
        return qimage

    def select_color(self):
        color = QColorDialog.getColor(self.color, self)
        if color.isValid():
            self.color = color
            self.apply_color_filter()

    def apply_color_filter(self):
        if self.adjusted_image:
            color_matrix = np.array([
                [1, 0, 0, self.color.red()],
                [0, 1, 0, self.color.green()],
                [0, 0, 1, self.color.blue()],
                [0, 0, 0, 1]
            ])

            # Convert the image to an array for manipulation
            img_array = np.array(self.adjusted_image)
            img_array = np.dot(img_array[...,:3], color_matrix[:3,:3].T) + color_matrix[:3,3]
            img_array = np.clip(img_array, 0, 255).astype(np.uint8)

            # Convert the array back to an image
            self.adjusted_image = Image.fromarray(img_array)
            self.display_image()

    def apply_adjustments(self):
        if self.pil_image:
            contrast = self.contrast_slider.value() / 100
            brightness = self.brightness_slider.value()

            # Apply contrast adjustment using Pillow
            enhancer = ImageEnhance.Contrast(self.pil_image)
            self.adjusted_image = enhancer.enhance(contrast)

            # Apply brightness adjustment
            enhancer = ImageEnhance.Brightness(self.adjusted_image)
            self.adjusted_image = enhancer.enhance(1 + brightness / 100)

            self.display_image()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageColorCustomizer()
    window.show()
    sys.exit(app.exec())

