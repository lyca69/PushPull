from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

import os, random, time, subprocess
from display import Ui_Form  # Pastikan Ui_Form memiliki textEdit

class MainController(QWidget):
    def __init__(self):
        super().__init__()  # Memanggil konstruktor QWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Menghubungkan tombol ke fungsi
        self.ui.pushButton.clicked.connect(self.save_text)
        self.ui.pushButton_2.clicked.connect(self.open_text)
    
    def save_text(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Simpan Catatan", "", "Text Files (*.txt);;All Files (*)")

        if file_name:
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(self.ui.textEdit.toPlainText())  # Perbaikan: self.text_edit -> self.ui.textEdit

    def open_text(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Buka Catatan", "", "Text Files (*.txt);;All Files (*)")

        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.ui.textEdit.setText(file.read())  # Perbaikan: self.text_edit -> self.ui.textEdit
