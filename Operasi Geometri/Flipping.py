import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt

# Sembunyikan jendela Tkinter
Tk().withdraw()

# Baca citra
file_path = askopenfilename()  # Tampilkan dialog pilihan file
image = cv2.imread(file_path)

# Pastikan gambar berhasil dibaca
if image is None:
    print("Gagal membaca gambar. Pastikan file ada dan formatnya didukung.")
else:
    # Dapatkan tinggi dan lebar citra
    height, width, _ = image.shape
    
    # Membuat citra pencerminan dengan slicing NumPy
    mirrored_image = image[:, ::-1]

    # Ubah format warna BGR ke RGB tanpa cv2.cvtColor()
    image_rgb = image[:, :, ::-1]
    mirrored_image_rgb = mirrored_image[:, :, ::-1]

    # Buat subplot untuk menampilkan gambar asli dan gambar pencerminan
    fig, axs = plt.subplots(1, 2)
    
    # Tampilkan gambar asli di subplot pertama
    axs[0].imshow(image_rgb)
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    
    # Tampilkan gambar pencerminan di subplot kedua
    axs[1].imshow(mirrored_image_rgb)
    axs[1].set_title('Mirrored Image')
    axs[1].axis('off')
    
    # Simpan gambar hasil flip horizontal
    cv2.imwrite("report/mirror_image.png", mirrored_image)

    # Tampilkan figure dengan subplot-subplotnya
    plt.show()
