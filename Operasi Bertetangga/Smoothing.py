import numpy as np
import cv2
import matplotlib.pyplot as plt

def main():
    # Baca citra
    image = cv2.imread('UTS-PCD/Images/bulan.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Lakukan penghalusan citra dengan rumus konvolusi langsung
    height, width = image.shape
    smoothed_image = np.zeros((height, width), dtype=np.uint8)
    
    # Mask smoothing 3x3
    mask = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]]) / 9.0
    
    # Lakukan konvolusi pada setiap piksel
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Ambil bagian citra yang sesuai dengan ukuran mask
            region = image[i-1:i+2, j-1:j+2]
            
            # Hitung nilai piksel baru dengan konvolusi menggunakan rumus
            smoothed_pixel = 0
            for m in range(3):
                for n in range(3):
                    smoothed_pixel += region[m, n] * mask[m, n]
            
            # Isi nilai piksel pada citra hasil
            smoothed_image[i, j] = int(smoothed_pixel)
    
    # Simpan citra hasil smoothing sebagai file baru
    cv2.imwrite('Output/Operasi-Bertetangga/hasil_penghalusan.jpg', smoothed_image)
    
    # Tampilkan citra asli dan hasilnya
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(cv2.imread('img/bulan.jpg'), cv2.COLOR_BGR2RGB))
    plt.title('Gambar Asli')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(cv2.imread('img-output/hasil_penghalusan.jpg'), cv2.COLOR_BGR2RGB))
    plt.title('Gambar Setelah Penghalusan')
    plt.axis('off')
    
    plt.show()

if __name__ == "__main__":
    main()
