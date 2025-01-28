import sys
from PyQt6.QtWidgets import QApplication
from controller import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainController()
    controller.show()
    sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog

# class SimpleNoteApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Aplikasi Catatan Sederhana")
#         self.setGeometry(100, 100, 600, 400)
        
#         # Membuat widget utama dan layout
#         self.text_edit = QTextEdit(self)
#         self.save_button = QPushButton("Simpan", self)
#         self.open_button = QPushButton("Buka", self)
        
#         # Menyusun layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.text_edit)
#         layout.addWidget(self.save_button)
#         layout.addWidget(self.open_button)
        
#         container = QWidget(self)
#         container.setLayout(layout)
#         self.setCentralWidget(container)
        
#         # Menambahkan koneksi tombol dengan fungsi
#         self.save_button.clicked.connect(self.save_file)
#         self.open_button.clicked.connect(self.open_file)

#     def save_file(self):
#         # Membuka dialog untuk memilih lokasi dan nama file untuk disimpan
#         file_name, _ = QFileDialog.getSaveFileName(self, "Simpan Catatan", "", "Text Files (*.txt);;All Files (*)")
        
#         if file_name:
#             # Menyimpan teks ke file
#             with open(file_name, 'w', encoding='utf-8') as file:
#                 file.write(self.text_edit.toPlainText())

#     def open_file(self):
#         # Membuka dialog untuk memilih file yang akan dibuka
#         file_name, _ = QFileDialog.getOpenFileName(self, "Buka Catatan", "", "Text Files (*.txt);;All Files (*)")
        
#         if file_name:
#             # Membaca file dan menampilkan teks ke QTextEdit
#             with open(file_name, 'r', encoding='utf-8') as file:
#                 self.text_edit.setText(file.read())

# # Fungsi utama untuk menjalankan aplikasi
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = SimpleNoteApp()
#     window.show()
#     sys.exit(app.exec())
