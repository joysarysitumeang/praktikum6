# praktikum 6

## program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa.

## flowchart 
<img width="792" height="952" alt="flowchart" src="https://github.com/user-attachments/assets/6d44fa5d-3d83-4a8b-ad5a-43cb62e6ef75" />


## penjelasan flowchart
- Alur Awal dan Loop: Program dimulai dan langsung masuk ke [Lingkaran] LOOP MENU UTAMA. Ini adalah perulangan tak terbatas (while True) yang memastikan program selalu siap menerima perintah.

- Keputusan Utama (Pilihan): Setelah menerima input Pilihan, alur program akan masuk ke serangkaian [Belah Ketupat] Keputusan. Ini adalah struktur percabangan (if-elif-else) yang menentukan aksi selanjutnya.

- Pemanggilan Fungsi: Ketika sebuah pilihan valid (1, 2, 3, atau 4) dipilih, alur program diarahkan ke [Persegi Panjang Bergaris], yang berarti terjadi pemanggilan fungsi (misalnya, tambah() atau ubah()). Fungsi ini kemudian menjalankan logikanya di cabang terpisah.

- Pengakhiran: Jika pengguna memilih Pilihan 5 (Keluar), alur program keluar dari loop dan berakhir di [Oval] SELESAI.

- Prinsip Modular: Struktur akar ini sangat efektif menunjukkan bahwa logika inti setiap operasi (seperti mencari dan menghapus data) diisolasi di Cabang Fungsi masing-masing, sementara Akar Utama hanya bertugas mengarahkan alur kendali.

## kode pemerograman python (praktikum6.py)
```py
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
```
## penjelasan kode python
1. Struktur Data (List of Dictionaries)
Program ini menggunakan sebuah List global bernama data_mahasiswa ([]). List ini bertindak sebagai database sementara yang menampung data. Setiap mahasiswa disimpan sebagai Dictionary di dalam List tersebut, yang memiliki pasangan key: value seperti 'nama' dan 'nilai'.

2. Fungsi Utama
Seluruh logika program dijalankan melalui lima bagian utama:

- main_menu(): Ini adalah fungsi pengendali utama yang menampilkan menu interaktif dan terus berulang (loop) sampai pengguna memilih keluar. Ia hanya bertugas menerima pilihan dan memanggil fungsi lain yang sesuai.

- tambah(): Fungsi ini menerima input nama dan nilai dari pengguna. Data tersebut kemudian dikemas dalam bentuk dictionary baru dan ditambahkan ke akhir data_mahasiswa menggunakan metode .append().

- tampilkan(): Fungsi ini memeriksa apakah data_mahasiswa kosong. Jika tidak, ia akan melakukan perulangan (loop) untuk menampilkan semua data nama dan nilai yang tersimpan secara terstruktur.

- hapus(nama): Fungsi ini menerima nama sebagai argumen. Ia kemudian menyaring (filter) atau mencari data di dalam data_mahasiswa yang namanya cocok dengan argumen yang diberikan, lalu menghapus data tersebut dari list.

- ubah(nama): Fungsi ini juga menerima nama sebagai argumen. Ia mencari data yang cocok. Jika ditemukan, ia meminta input nilai_baru dari pengguna, kemudian mengubah (update) nilai lama di dictionary tersebut dengan nilai yang baru.

- Intinya, pemrograman ini menekankan pada penggunaan fungsi untuk membuat kode yang rapi, mudah dikelola, dan setiap fungsi hanya melakukan satu tugas (misalnya, tambah() hanya menambah, tidak menampilkan).

## output
<img width="1902" height="1079" alt="Screenshot 2025-11-29 225956" src="https://github.com/user-attachments/assets/11d56a9a-b8b7-40e0-b0ed-eeaa99689ddb" />
<img width="1919" height="502" alt="Screenshot 2025-11-29 230046" src="https://github.com/user-attachments/assets/a231eee5-0170-4f27-b257-b5a39cbc6f30" />
<img width="1915" height="469" alt="Screenshot 2025-11-29 230114" src="https://github.com/user-attachments/assets/c8507989-8702-40d3-9c52-41a3b81422af" />
<img width="1860" height="1050" alt="Screenshot 2025-11-29 230312" src="https://github.com/user-attachments/assets/9e840aac-72a8-42fd-9d31-06af0d037783" />

