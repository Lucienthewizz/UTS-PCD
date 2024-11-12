from PIL import Image  # Mengimpor modul Image dari PIL (Python Imaging Library)
import numpy as np  # Mengimpor modul numpy untuk manipulasi array
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari matplotlib untuk plotting

# Fungsi untuk meningkatkan kontras gambar menggunakan array dengan looping
def enhance_contrast(image, G, P):
    img_array = np.array(image, dtype=np.int32)  # Ubah gambar menjadi array numpy
    tinggi, lebar = img_array.shape  # Dapatkan ukuran gambar

    # Loop untuk menghitung nilai kontras baru untuk setiap piksel (x, y)
    for x in range(tinggi):  # Loop untuk setiap baris
        for y in range(lebar):  # Loop untuk setiap kolom
            current_value = img_array[x, y]  # Mengambil nilai piksel saat ini
            # Menghitung nilai kontras baru
            new_value = G * (current_value - P) + P
            
            # Membatasi nilai baru antara 0 dan 255
            if new_value > 255:  # Jika nilai baru lebih dari 255
                new_value = 255  # Set nilai baru ke 255
            elif new_value < 0:  # Jika nilai baru kurang dari 0
                new_value = 0  # Set nilai baru ke 0
            
            # Memasukkan nilai piksel yang baru
            img_array[x, y] = new_value

    return Image.fromarray(img_array.astype(np.uint8))  # Ubah kembali ke tipe uint8

# Fungsi untuk menampilkan histogram gambar
def plot_histogram(image, title, G, P):
    hist_data = list(image.getdata())
    plt.bar(range(256), [hist_data.count(i) for i in range(256)], width=1, color='gray', alpha=0.7)
    plt.title(f"{title} (G = {G}, P = {P})")  # Menampilkan G dan P pada judul histogram
    plt.xlim([0, 255])  # Mengatur batas sumbu x
    plt.xlabel('Nilai Piksel')  # Label sumbu x
    plt.ylabel('Frekuensi')  # Label sumbu y
    plt.grid(True)  # Menampilkan grid pada histogram

# Fungsi utama untuk menjalankan peningkatan kontras dan menampilkan gambar
def main(image_path, G, P):
    # Membaca gambar
    image = Image.open(image_path)

    # Mengecek apakah gambar sudah grayscale, jika tidak maka konversi
    if image.mode != 'L':
        print("Gambar bukan grayscale, mengonversi ke grayscale.")
        image = image.convert('L')
    else:
        print("Gambar sudah grayscale, tidak perlu dikonversi.")

    # Melakukan peningkatan kontras
    contrast_image = enhance_contrast(image.copy(), G, P)

    # Menyiapkan figure dengan ukuran yang sesuai
    plt.figure(figsize=(12, 10))

    # Menampilkan gambar asli
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.title('Gambar Asli')
    plt.axis('off')

    # Menampilkan histogram sebelum peningkatan kontras
    plt.subplot(2, 2, 2)
    plot_histogram(image, 'Histogram Sebelum Peningkatan Kontras', G, P)

    # Menampilkan gambar dengan kontras yang ditingkatkan
    plt.subplot(2, 2, 3)
    plt.imshow(contrast_image, cmap='gray', interpolation='nearest')
    plt.title('Gambar Setelah Peningkatan Kontras')
    plt.axis('off')

    # Menampilkan histogram setelah peningkatan kontras
    plt.subplot(2, 2, 4)
    plot_histogram(contrast_image, 'Histogram Setelah Peningkatan Kontras', G, P)

    plt.tight_layout()  # Mengatur tata letak agar tidak saling tumpang tindih
    plt.show()

# Ganti 'your_image_path' dengan path gambar yang ingin diproses
G = 1.5  # Koefisien penguatan kontras
P = 128  # Nilai pusat pengontrasan
main('Images/image-1_1.jpg', G, P)  # Ganti dengan path gambar Anda
