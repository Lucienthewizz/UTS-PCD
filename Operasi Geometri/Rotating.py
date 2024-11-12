from PIL import Image

# Load gambar asli
gambar_asli = Image.open("Images/RGB.jpg")

# Konversi gambar asli ke mode "RGB"
gambar_asli = gambar_asli.convert("RGB")

# Mendapatkan ukuran gambar
w, h = gambar_asli.size

# Membuat gambar-gambar hasil rotasi
gambar_rotasi_90 = Image.new("RGB", (h, w))
gambar_rotasi_180 = Image.new("RGB", (w, h))
gambar_rotasi_270 = Image.new("RGB", (h, w))

# Menentukan koordinat 0,0 dari gambar asli
koordinat_asli_0_0 = (0, 0)
print(f"Koordinat 0,0 dari gambar asli: {koordinat_asli_0_0}")

# Fungsi untuk mendapatkan koordinat asli sebelum rotasi
def get_original_coordinate(x, y, width, height, degree):
    if degree == 90:
        return (height - y - 1, x)  # Koordinat asli sebelum rotasi 90 derajat
    elif degree == 180:
        return (width - x - 1, height - y - 1)  # Koordinat asli sebelum rotasi 180 derajat
    elif degree == 270:
        return (y, width - x - 1)  # Koordinat asli sebelum rotasi 270 derajat
    else:
        return (x, y)  # Tidak ada rotasi

# Proses rotasi untuk setiap derajat
for x in range(w):
    for y in range(h):
        piksel_asli = gambar_asli.getpixel((x, y))

        # Rotasi 90 derajat searah jarum jam
        gambar_rotasi_90.putpixel((h - y - 1, x), piksel_asli)

        # Rotasi 180 derajat
        gambar_rotasi_180.putpixel((w - x - 1, h - y - 1), piksel_asli)

        # Rotasi 270 derajat searah jarum jam
        gambar_rotasi_270.putpixel((y, w - x - 1), piksel_asli)

# Mendapatkan koordinat asli untuk posisi (0,0) setelah setiap rotasi
koordinat_asli_setelah_rotasi_90 = get_original_coordinate(0, 0, w, h, 90)
koordinat_asli_setelah_rotasi_180 = get_original_coordinate(0, 0, w, h, 180)
koordinat_asli_setelah_rotasi_270 = get_original_coordinate(0, 0, w, h, 270)

# Menampilkan koordinat asli dari gambar yang sudah dirotasi
print(f"Koordinat asli dari posisi (0,0) pada gambar rotasi 90 derajat: {koordinat_asli_setelah_rotasi_90}")
print(f"Koordinat asli dari posisi (0,0) pada gambar rotasi 180 derajat: {koordinat_asli_setelah_rotasi_180}")
print(f"Koordinat asli dari posisi (0,0) pada gambar rotasi 270 derajat: {koordinat_asli_setelah_rotasi_270}")

# Menyimpan gambar hasil rotasi
gambar_rotasi_90.save("Output/rotasi90.png")
gambar_rotasi_180.save("Output/rotasi180.png")
gambar_rotasi_270.save("Output/rotasi270.png")
print("Gambar rotasi berhasil disimpan")

# Komparasi koordinat dari gambar asli dan yang sudah dirotate
print("Komparasi Koordinat:")
print(f"Koordinat asli: {koordinat_asli_0_0}")
print(f"Koordinat setelah rotasi 90 derajat: {koordinat_asli_setelah_rotasi_90}")
print(f"Koordinat setelah rotasi 180 derajat: {koordinat_asli_setelah_rotasi_180}")
print(f"Koordinat setelah rotasi 270 derajat: {koordinat_asli_setelah_rotasi_270}")
