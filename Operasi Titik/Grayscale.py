from PIL import Image

# Buka citra RGB
rgb_image = Image.open("UTS-PCD/Images/RGB.jpg")

# Konversi citra RGB menjadi citra grayscale
gray_image = Image.new("L", rgb_image.size)  # Buat citra baru dengan mode "L" (grayscale)

# Loop melalui setiap piksel pada citra RGB dan konversi ke grayscale
for x in range(rgb_image.width):
    for y in range(rgb_image.height):
        r, g, b = rgb_image.getpixel((x, y))
        grayscale_value = int(round((0.299 * r) + (0.587 * g) + (0.114 * b)))
        gray_image.putpixel((x, y), grayscale_value)

# Simpan citra grayscale
output_path = "UTS-PCD/Output/grayscale_output.png"
gray_image.save(output_path)

# Cetak pesan sukses jika citra berhasil disimpan
print(f"Grayscale image saved successfully at {output_path}")

# Tutup citra
rgb_image.close()
