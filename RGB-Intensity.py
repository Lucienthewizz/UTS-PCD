import cv2

# Memuat gambar (ganti 'Output/rotas180.png' dengan path gambar yang sesuai)
image_path = 'Output/rotas180.png'
output_file = 'Output/intens_RGB_180.txt'  # Tentukan nama file output

# Membaca gambar menggunakan OpenCV
image = cv2.imread(image_path)

# Periksa apakah gambar berhasil dimuat
if image is None:
    print("Error: Tidak dapat memuat gambar.")
else:
    # Dapatkan dimensi gambar
    height = image.shape[0]
    width = image.shape[1]

    # Buka file output untuk menulis
    with open(output_file, 'w') as file:
        # Keluarkan intensitas RGB dan koordinat masing-masing piksel
        for y in range(height):
            for x in range(width):
                # Dapatkan nilai RGB piksel
                r = image[y, x][2]
                g = image[y, x][1]
                b = image[y, x][0]

                # Hitung intensitas
                intensity = round((0.299 * r) + (0.587 * g) + (0.114 * b))

                # Keluarkan intensitas dan koordinat
                file.write(f"({x},{y}) => R: {r}, G: {g}, B: {b}, Intensity: {intensity}\n")

    # Cetak pesan sukses
    print(f"Nilai intensitas RGB berhasil disimpan ke {output_file}")

    # Tampilkan gambar
    cv2.waitKey(0)  # Tunggu sampai tombol ditekan
    cv2.destroyAllWindows()

