class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    def tampilkan(self):
        return f"{self.nim} - {self.nama} ({self.jurusan})"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, mhs):
        self.data.append(mhs)

    def tampilkan_semua(self):
        hasil = []
        for mhs in self.data:
            hasil.append(mhs.tampilkan())
        return hasil


# penggunaan
data = DataMahasiswa()

while True:
    print("\n1. Tambah Mahasiswa")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama: ")
        nim = input("NIM: ")
        jurusan = input("Jurusan: ")
        data.tambah(Mahasiswa(nama, nim, jurusan))
        print("Data berhasil ditambahkan")

    elif pilihan == "2":
        for d in data.tampilkan_semua():
            print(d)

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid")
