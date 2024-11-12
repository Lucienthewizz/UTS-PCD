import numpy as np
import matplotlib.pyplot as plt
import cv2

# Membaca citra input dari file
img = cv2.imread("Images/berasREAL.jpg", cv2.IMREAD_GRAYSCALE)

# Operator Roberts
kernel_x = np.array([[1, 0], [0, -1]])
kernel_y = np.array([[0, 1], [-1, 0]])

# Matriks output
output = np.zeros_like(img)

# Hitung gradien intensitas
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        Gx = np.sum(kernel_x * img[i:i + 2, j:j + 2])
        Gy = np.sum(kernel_y * img[i:i + 2, j:j + 2])
        output[i, j] = np.sqrt(Gx ** 2 + Gy ** 2)

# Gunakan nilai intensitas maksimum
max_val = np.max(output)
for i in range(output.shape[0]):
    for j in range(output.shape[1]):
        output[i, j] = max(output[i, j], 0)

# Menyimpan citra tepi ke file baru
plt.imsave("Output/Operasi-Bertetangga/hasil_tepi (Robert).jpg", output, cmap="gray")

# Membuat histogram untuk citra asli dan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Citra Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(output, cmap='gray')
plt.title('Hasil Tepi')
plt.axis('off')

# Membuat histogram untuk citra asli dan hasil
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, [0, 256], color='gray')
plt.title('Histogram Citra Asli')
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')

plt.subplot(1, 2, 2)
plt.hist(output.ravel(), 256, [0, 256], color='gray')
plt.title('Histogram Hasil Tepi')
plt.xlabel('Nilai Piksel')
plt.ylabel('Frekuensi')

# Perbandingan gambar asli dan setelah berubah
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(cv2.imread("img/berasREAL.jpg"), cv2.COLOR_BGR2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cv2.imread("img-output/hasil_tepi (Robert).jpg"), cv2.COLOR_BGR2RGB))
plt.title('Gambar Setelah Berubah')
plt.axis('off')

plt.show()
