from PIL import Image  # Mengimpor modul Image dari PIL (Python Imaging Library)
import numpy as np  # Mengimpor modul numpy untuk manipulasi array
import matplotlib.pyplot as plt  # Mengimpor modul pyplot dari matplotlib untuk plotting

# Fungsi untuk melakukan negasi gambar menggunakan array dengan looping
def negate_image(image):
    img_array = np.array(image, dtype=np.int32)  # Ubah gambar menjadi array numpy
    tinggi, lebar = img_array.shape  # Dapatkan ukuran gambar

    # Loop untuk menghitung nilai negasi untuk setiap piksel (x, y)
    for x in range(tinggi):  # Loop untuk setiap baris
        for y in range(lebar):  # Loop untuk setiap kolom
            current_value = img_array[x, y]  # Mengambil nilai piksel saat ini
            new_value = 255 - current_value  # Menghitung nilai negasi
            
            # Memasukkan nilai piksel yang baru
            img_array[x, y] = new_value

    return Image.fromarray(img_array.astype(np.uint8))  # Ubah kembali ke tipe uint8

# Fungsi untuk menampilkan histogram gambar
def plot_histogram(image, title):
    hist_data = list(image.getdata())  # Mengambil data piksel untuk histogram
    plt.bar(range(256), [hist_data.count(i) for i in range(256)], width=1, color='gray', alpha=0.7)
    plt.title(title)  # Judul histogram
    plt.xlim([0, 255])  # Mengatur batas sumbu x
    plt.xlabel('Nilai Piksel')  # Label sumbu x
    plt.ylabel('Frekuensi')  # Label sumbu y
    plt.grid(True)  # Menampilkan grid pada histogram

# Fungsi utama untuk menjalankan negasi dan menampilkan gambar
def main(image_path):
    # Membaca gambar
    image = Image.open(image_path)

    # Mengecek apakah gambar sudah grayscale, jika tidak maka konversi
    if image.mode != 'L':
        print("Gambar bukan grayscale, mengonversi ke grayscale.")
        image = image.convert('L')
    else:
        print("Gambar sudah grayscale, tidak perlu dikonversi.")

    # Melakukan negasi
    negated_image = negate_image(image.copy())

    # Menyiapkan figure dengan ukuran yang sesuai
    plt.figure(figsize=(12, 10))

    # Menampilkan gambar asli
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.title('Gambar Asli')
    plt.axis('off')

    # Menampilkan histogram sebelum negasi
    plt.subplot(2, 2, 2)
    plot_histogram(image, 'Histogram Sebelum Negasi')

    # Menampilkan gambar negasi
    plt.subplot(2, 2, 3)
    plt.imshow(negated_image, cmap='gray', interpolation='nearest')
    plt.title('Gambar Negasi')
    plt.axis('off')

    # Menampilkan histogram setelah negasi
    plt.subplot(2, 2, 4)
    plot_histogram(negated_image, 'Histogram Setelah Negasi')

    plt.tight_layout()  # Mengatur tata letak agar tidak saling tumpang tindih
    plt.show()

# Ganti 'your_image_path' dengan path gambar yang ingin diproses
main('Images/image-1_1.jpg')  # Ganti dengan path gambar Anda

