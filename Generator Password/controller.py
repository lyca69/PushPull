from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from display import Ui_Form
import random

class MainController(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.spinBox.setRange(4,32)
        self.ui.spinBox.setValue(12)

        self.ui.checkBox.setChecked(True)
        self.ui.checkBox_2.setChecked(True)
        self.ui.checkBox_3.setChecked(True)
        self.ui.checkBox_4.setChecked(True)

        self.ui.pushButton.clicked.connect(self.generate)#Generate Button
        
        self.ui.lineEdit.setReadOnly(True)

        self.ui.pushButton_2.clicked.connect(self.copy)#Copy Button

    
    def generate(self):
        character=''
        if self.ui.checkBox.isChecked():
            character += 'abcdefghijklmnopqrstuvwxyz'
        if self.ui.checkBox_2.isChecked():
            character += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if self.ui.checkBox_3.isChecked():
            character += '0123456789'
        if self.ui.checkBox_4.isChecked():
            character += '!@#$%&*?'

        if not character :
            self.ui.lineEdit.setText('Pilih setidaknya 1 opsi  karakter!')
        
        length = self.ui.spinBox.value()
        password=''.join(random.choice(character) for _ in range(length))
        self.ui.lineEdit.setText(password)

    def copy(self):
        clipboard=QApplication.clipboard()
        clipboard.setText(self.ui.lineEdit.text())

