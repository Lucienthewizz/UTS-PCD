from PIL import Image, ExifTags

# Path ke gambar
imagename = "UTS-PCD/Images/RGB.jpg"

# Membaca data gambar menggunakan PIL
image = Image.open(imagename)

# Mengekstrak metadata dasar
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")

# Mengekstrak data EXIF
exifdata = image.getexif()

# Iterasi melalui semua bidang data EXIF
for tag_id in exifdata:
    # Dapatkan nama tag, alih-alih id tag yang sulit dibaca manusia
    tag = ExifTags.TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)

    # Dekodekan bytes
    if isinstance(data, bytes):
        data = data.decode()

    print(f"{tag:25}: {data}")
