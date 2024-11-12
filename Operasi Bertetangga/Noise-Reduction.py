import cv2
import numpy as np
import matplotlib.pyplot as plt

def convolution_median(image):
    # Mendapatkan ukuran gambar
    height, width = image.shape
    # Menyiapkan output gambar
    result = np.zeros_like(image)
    
    # Menentukan ukuran masking
    mask_size = 3
    
    # Looping untuk setiap piksel dalam gambar
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Mendapatkan nilai piksel di sekitar piksel yang sedang diproses
            neighbors = [
                image[i - 1, j - 1], image[i - 1, j], image[i - 1, j + 1],
                image[i, j - 1], image[i, j], image[i, j + 1],
                image[i + 1, j - 1], image[i + 1, j], image[i + 1, j + 1]
            ]
            
            # Melakukan konvolusi dengan metode median tanpa menggunakan fungsi
            for k in range(len(neighbors)):
                for l in range(k, len(neighbors)):
                    if neighbors[k] > neighbors[l]:
                        neighbors[k], neighbors[l] = neighbors[l], neighbors[k]
            
            # Ambil nilai median, yang berada pada indeks ke-4 setelah diurutkan
            result[i, j] = neighbors[4]
    
    return result

# Membaca gambar
image_path = 'Images/albert.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Melakukan konvolusi dengan metode median
result_image = convolution_median(original_image)

# Menyimpan hasil konvolusi ke dalam file gambar
output_path = 'Output/Operasi-Bertetangga/hasil_noise_reduction.jpg'
cv2.imwrite(output_path, result_image)

# Menampilkan perbandingan gambar asli dan hasil konvolusi
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_GRAY2RGB))
plt.title('Gambar Asli')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(result_image, cv2.COLOR_GRAY2RGB))
plt.title('Gambar Setelah Konvolusi')
plt.axis('off')

plt.show()

print(f'Hasil konvolusi disimpan di: {output_path}')
