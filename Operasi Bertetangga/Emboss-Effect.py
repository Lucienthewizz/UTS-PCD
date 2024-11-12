import numpy as np
import cv2
import matplotlib.pyplot as plt

# Membaca citra input dalam grayscale
img = cv2.imread("UTS-PCD/Images/bulan.jpg", cv2.IMREAD_GRAYSCALE)

# Dimensi citra
height, width = img.shape

# Konversi sementara ke int16 untuk mencegah overflow
temp_img = img.astype(np.int16)

# Matriks output
output = np.zeros_like(temp_img)

# Kernel emboss
kernel = np.array([[-1, -1, 0],
                   [-1, 1, 1],
                   [0, 1, 1]])

# Mengaplikasikan efek emboss
for i in range(1, height - 1):
    for j in range(1, width - 1):
        region = temp_img[i-1:i+2, j-1:j+2]
        output[i, j] = np.sum(region * kernel)

# Menyaring nilai output agar tetap dalam rentang [0, 255]
output = np.clip(output, 0, 255).astype(np.uint8)

# Menyimpan hasil citra dengan efek emboss
plt.imsave("UTS-PCD/Output/Operasi-Bertetangga/hasil_timbul.jpg", output, cmap="gray")

# Menampilkan perbandingan gambar asli dan setelah emboss
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(cv2.imread("img/bulan.jpg"), cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cv2.imread("img-output/hasil_timbul.jpg"), cv2.COLOR_BGR2RGB))
plt.title('Gambar Setelah Berubah')
plt.axis('off')

plt.show()
