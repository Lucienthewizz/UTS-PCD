import cv2

# Muat gambar (ganti 'UTS-PCD/Output/rotas180.png' dengan path gambar yang sesuai)
image_path = 'Output/rotas180.png'
output_file = 'Output/intens_grayscale_180.txt'  # Tentukan nama file output

# Baca gambar menggunakan OpenCV
image = cv2.imread(image_path)

# Cek apakah gambar berhasil dimuat
if image is None:
    print("Error: Tidak dapat memuat gambar.")
else:
    # Dapatkan dimensi gambar
    height = image.shape[0]
    width = image.shape[1]

    # Buka file output untuk menulis
    with open(output_file, 'w') as file:
        # Keluarkan intensitas grayscale dan koordinat masing-masing piksel
        for y in range(height):
            for x in range(width):
                # Dapatkan nilai RGB piksel
                r = image[y, x][2]
                g = image[y, x][1]
                b = image[y, x][0]

                # Hitung intensitas grayscale secara manual
                # Rumus intensitas grayscale: 0.299*R + 0.587*G + 0.114*B
                intensity = int(round((0.299 * r) + (0.587 * g) + (0.114 * b)))

                # Keluarkan intensitas dan koordinat
                file.write(f"({x},{y}) => Intensitas: {intensity}\n")

    # Cetak pesan sukses
    print(f"Nilai intensitas grayscale berhasil disimpan ke {output_file}")

    # Konversikan gambar ke grayscale secara manual untuk tujuan tampilan
    # Membuat gambar baru dengan dimensi yang sama, tetapi single channel (grayscale)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for y in range(height):
        for x in range(width):
            grayscale_image[y, x] = int(round((0.299 * image[y, x][2]) + 
                                              (0.587 * image[y, x][1]) + 
                                              (0.114 * image[y, x][0])))

    # Tampilkan gambar grayscale
    cv2.waitKey(0)  # Tunggu sampai tombol ditekan
    cv2.destroyAllWindows()

