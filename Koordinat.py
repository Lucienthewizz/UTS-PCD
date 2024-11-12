from PIL import Image
import numpy as np

def cetak_koordinat(gambar):
    img_array = np.array(gambar, dtype=np.int32)  # Ubah gambar menjadi array numpy
    tinggi, lebar = img_array.shape  # Dapatkan ukuran gambar

    # Loop untuk mencetak koordinat setiap piksel
    for x in range(tinggi):
        for y in range(lebar):
            # Cetak koordinat dan nilai piksel asli
            print(f"Koordinat f({x}, {y}) = Nilai Kecerahan: {img_array[x, y]}")

def main(image_path):
    # Membaca gambar
    gambar = Image.open(image_path)

    # Mengecek apakah gambar sudah grayscale, jika tidak maka konversi
    if gambar.mode != 'L':
        print("Gambar bukan grayscale, mengonversi ke grayscale.")
        gambar = gambar.convert('L')
    else:
        print("Gambar sudah grayscale, tidak perlu dikonversi.")

    # Mencetak koordinat dan nilai kecerahan piksel
    cetak_koordinat(gambar)

# Ganti 'your_image_path' dengan path gambar yang ingin diproses
main('Images/image-1.jpg')  # Ganti dengan path gambar Anda
