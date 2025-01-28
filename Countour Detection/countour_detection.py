import numpy as np
import cv2

# Membaca gambar
img = cv2.imread("C:\Users\ASUS\Documents\Python_LTI\Countour Detection\ba.jpg")
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Menggunakan adaptive thresholding untuk meningkatkan deteksi objek
adaptive_threshold = cv2.adaptiveThreshold(imggray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Menggunakan Canny edge detection untuk deteksi tepi
edges = cv2.Canny(imggray, 50, 150)

# Menyaring kontur berdasarkan luas objek
contours, hierarchy = cv2.findContours(adaptive_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = [c for c in contours if cv2.contourArea(c) > 100]  # Menyaring berdasarkan area kontur

# Menggambar kontur di atas gambar asli
cv2.drawContours(img, contours, -1, (0, 255, 0), 1)

# Menggunakan operasi morfologi untuk memperhalus kontur (opsional)
kernel = np.ones((3, 3), np.uint8)
processed_img = cv2.erode(edges, kernel, iterations=1)
processed_img = cv2.dilate(processed_img, kernel, iterations=1)

# Mengubah ukuran gambar menjadi 800x600
img_resized = cv2.resize(img, (800, 600))
imggray_resized = cv2.resize(imggray, (800, 600))
adaptive_threshold_resized = cv2.resize(adaptive_threshold, (800, 600))

#Menampilkan jumlah contour pada gambar
print("Number of contours : "+str(len(contours)))

# Menampilkan hasil
cv2.imshow('Original Image with Contours', img_resized)
cv2.imshow('Gray Image', imggray_resized)
cv2.imshow('Adaptive Threshold', adaptive_threshold_resized)
cv2.imshow('Canny Edge Detection', edges)
cv2.imshow('Processed Image (Canny + Morphology)', processed_img)

cv2.waitKey(0)
cv2.destroyAllWindows()