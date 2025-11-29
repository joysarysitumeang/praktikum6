# List untuk menyimpan data mahasiswa
mahasiswa = []

# Fungsi untuk menambah data
def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Masukkan nama   : ")
    nilai = float(input("Masukkan nilai  : "))
    
    mahasiswa.append({"nama": nama, "nilai": nilai})
    print("Data berhasil ditambahkan!\n")

# Fungsi untuk menampilkan data
def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not mahasiswa:
        print("Belum ada data.\n")
    else:
        for i, mhs in enumerate(mahasiswa, start=1):
            print(f"{i}. Nama: {mhs['nama']} - Nilai: {mhs['nilai']}")
        print()

# Fungsi untuk menghapus data berdasarkan nama
def hapus(nama):
    print("\n=== Hapus Data Mahasiswa ===")
    for mhs in mahasiswa:
        if mhs["nama"].lower() == nama.lower():
            mahasiswa.remove(mhs)
            print("Data berhasil dihapus!\n")
            return
    print("Data dengan nama tersebut tidak ditemukan.\n")

# Fungsi untuk mengubah data berdasarkan nama
def ubah(nama):
    print("\n=== Ubah Data Mahasiswa ===")
    for mhs in mahasiswa:
        if mhs["nama"].lower() == nama.lower():
            new_nama = input("Masukkan nama baru   : ")
            new_nilai = float(input("Masukkan nilai baru  : "))
            mhs["nama"] = new_nama
            mhs["nilai"] = new_nilai
            print("Data berhasil diubah!\n")
            return
    print("Data dengan nama tersebut tidak ditemukan.\n")

# Menu utama
while True:
    print("===== MENU =====")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama yang akan dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama yang akan diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid!\n")
