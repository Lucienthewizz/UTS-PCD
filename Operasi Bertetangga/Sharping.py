import cv2
import numpy as np
import matplotlib.pyplot as plt

def sharpen_image(image):
    height, width = image.shape
    # Mask sharpening 3x3 dengan α = 1
    mask = np.array([[-1, -1, -1],
                     [-1, 9, -1],
                     [-1, -1, -1]])
    
    # Buat citra hasil dengan ukuran yang sama
    sharpened_image = np.zeros((height, width), dtype=np.uint8)
    
    # Lakukan konvolusi pada setiap piksel
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            # Ambil bagian citra yang sesuai dengan ukuran mask
            region = image[i-1:i+2, j-1:j+2]
            
            # Hitung nilai piksel baru dengan konvolusi
            sharpened_pixel = 0
            for m in range(3):
                for n in range(3):
                    sharpened_pixel += region[m, n] * mask[m, n]
            
            # Isi nilai piksel pada citra hasil
            sharpened_image[i, j] = np.clip(sharpened_pixel, 0, 255).astype(np.uint8)
    
    return sharpened_image

def main():
    # Baca citra
    image = cv2.imread('Images/bulan.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Sharpen citra
    sharpened_image = sharpen_image(image)

    # Simpan citra hasil sharpening sebagai file baru
    cv2.imwrite('Output/Operasi-Bertetangga/hasil_penajaman.jpg', sharpened_image)
    
    # Tampilkan panel figure
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Gambar Asli')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
    plt.title('Gambar Setelah Penajaman')
    plt.axis('off')
    
    plt.show()

if __name__ == "__main__":
    main()
