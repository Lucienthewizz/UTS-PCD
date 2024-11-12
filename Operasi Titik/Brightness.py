from PIL import Image  # Mengimpor modul Image dari PIL (Python Imaging Library)
import numpy as np  # Mengimpor modul numpy untuk manipulasi array
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari matplotlib untuk plotting

# Fungsi untuk menyesuaikan kecerahan gambar menggunakan array dengan looping
def adjust_brightness(image, c):
    img_array = np.array(image, dtype=np.int32)  # Ubah gambar menjadi array numpy
    tinggi, lebar = img_array.shape  # Dapatkan ukuran gambar

    # Loop untuk menambah nilai C ke setiap piksel (x, y)
    for x in range(tinggi):  # Loop untuk setiap baris
        for y in range(lebar):  # Loop untuk setiap kolom
            # Mengambil nilai piksel saat ini
            current_value = img_array[x, y]
            # Menghitung nilai baru dengan rumus: K_o = K_i + C
            new_value = current_value + c  
            # Membatasi nilai baru antara 0 dan 255
            if new_value > 255:  # Jika nilai baru lebih dari 255
                new_value = 255  # Set nilai baru ke 255
            elif new_value < 0:  # Jika nilai baru kurang dari 0
                new_value = 0  # Set nilai baru ke 0
            
            # Memasukkan nilai piksel yang baru
            img_array[x, y] = new_value

    return Image.fromarray(img_array.astype(np.uint8))  # Ubah kembali ke tipe uint8

# Fungsi untuk menampilkan histogram gambar
def plot_histogram(image, title, c):
    hist_data = list(image.getdata())
    plt.bar(range(256), [hist_data.count(i) for i in range(256)], width=1, color='gray', alpha=0.7)
    plt.title(f"{title} (c = {c})")  # Menampilkan c pada judul histogram
    plt.xlim([0, 255])  # Mengatur batas sumbu x
    plt.xlabel('Nilai Piksel')  # Label sumbu x
    plt.ylabel('Frekuensi')  # Label sumbu y
    plt.grid(True)  # Menampilkan grid pada histogram

# Fungsi utama untuk menjalankan penyesuaian kecerahan dan menampilkan gambar
def main(image_path, c):
    # Membaca gambar
    image = Image.open(image_path)

    # Mengecek apakah gambar sudah grayscale, jika tidak maka konversi
    if image.mode != 'L':
        print("Gambar bukan grayscale, mengonversi ke grayscale.")
        image = image.convert('L')
    else:
        print("Gambar sudah grayscale, tidak perlu dikonversi.")

    # Melakukan penyesuaian kecerahan
    adjusted_image = adjust_brightness(image.copy(), c)

    # Menyiapkan figure dengan ukuran yang sesuai
    plt.figure(figsize=(12, 10))

    # Menampilkan gambar asli
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.title('Gambar Asli')
    plt.axis('off')

    # Menampilkan histogram sebelum penyesuaian
    plt.subplot(2, 2, 2)
    plot_histogram(image, 'Histogram Sebelum Penyesuaian', c)

    # Menampilkan gambar setelah penyesuaian
    plt.subplot(2, 2, 3)
    plt.imshow(adjusted_image, cmap='gray', interpolation='nearest')
    plt.title('Gambar Setelah Penyesuaian')
    plt.axis('off')

    # Menampilkan histogram setelah penyesuaian
    plt.subplot(2, 2, 4)
    plot_histogram(adjusted_image, 'Histogram Setelah Penyesuaian', c)

    plt.tight_layout()  # Mengatur tata letak agar tidak saling tumpang tindih
    plt.show()

# Ganti 'your_image_path' dengan path gambar yang ingin diproses
main('Images/image-1_1.jpg', c=50)  # Ganti dengan path gambar Anda dan nilai c yang diinginkan


