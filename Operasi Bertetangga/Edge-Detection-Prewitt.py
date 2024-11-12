import numpy as np
import matplotlib.pyplot as plt
import cv2

# Membaca citra input dari file
img = cv2.imread("Images/berasREAL.jpg", cv2.IMREAD_GRAYSCALE)

# Pastikan gambar berhasil dibaca
if img is None:
    print("Gambar tidak ditemukan.")
else:
    # Operator Prewitt
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

    # Matriks output dengan ukuran yang sama seperti input, tapi lebih kecil untuk menghindari tepi
    output = np.zeros_like(img, dtype=np.float32)

    # Iterasi dengan mengecualikan batas tepi gambar
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            # Hitung gradien Gx dan Gy dengan kernel Prewitt
            Gx = np.sum(kernel_x * img[i-1:i+2, j-1:j+2])
            Gy = np.sum(kernel_y * img[i-1:i+2, j-1:j+2])

            # Magnitudo gradien
            output[i, j] = np.sqrt(Gx**2 + Gy**2)

    # Normalisasi nilai output ke dalam rentang [0, 255] dan konversi ke uint8
    output = np.clip(output, 0, 255).astype(np.uint8)

    # Menyimpan citra hasil ke file
    plt.imsave("Output/Operasi-Bertetangga/hasil_tepi (Prewitt).jpg", output, cmap="gray")
    print("Proses deteksi tepi selesai dan hasil disimpan.")

    # Perbandingan gambar asli dan setelah
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(cv2.imread("img/berasREAL.jpg"), cv2.COLOR_BGR2RGB))
    plt.title('Gambar Asli')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(cv2.imread("img-output/hasil_tepi (Prewitt).jpg"), cv2.COLOR_BGR2RGB))
    plt.title('Gambar Setelah Berubah')
    plt.axis('off')

    plt.show()
