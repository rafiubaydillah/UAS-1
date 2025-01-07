# Aplikasi Pengelolaan Data Pengguna

Aplikasi ini adalah program sederhana yang memungkinkan pengguna untuk memasukkan nama dan usia, kemudian menampilkan data tersebut dalam format tabel. Program ini ditulis dalam bahasa pemrograman Python dan terdiri dari tiga kelas utama: `Data`, `View`, dan `Process`.

## Struktur Kode

### 1. Kelas `Data`

Kelas ini bertanggung jawab untuk menyimpan dan mengelola entri pengguna.

#### Metode:
- **`__init__(self)`**: Konstruktor yang menginisialisasi daftar kosong untuk menyimpan entri pengguna.
- **`add_entry(self, name, age)`**: Menambahkan entri baru ke dalam daftar dengan nama dan usia yang diberikan.
- **`get_entries(self)`**: Mengembalikan semua entri yang telah dimasukkan.

### 2. Kelas `View`

Kelas ini mengelola tampilan data yang akan ditampilkan kepada pengguna.

#### Metode:
- **`display_table(entries)`**: Metode statis yang menerima daftar entri dan mencetaknya dalam format tabel. Tabel terdiri dari dua kolom: "Nama" dan "Usia".

### 3. Kelas `Process`

Kelas ini berfungsi sebagai penghubung antara input pengguna dan tampilan data.

#### Metode:
- **`__init__(self)`**: Konstruktor yang menginisialisasi objek dari kelas `Data` dan `View`.
- **`get_user_input(self)`**: Mengambil input dari pengguna dalam bentuk nama dan usia. Program akan terus meminta input hingga pengguna mengetik 'exit'. Metode ini juga melakukan validasi input, memastikan usia adalah angka positif.
- **`display_results(self)`**: Mengambil entri dari kelas `Data` dan memanggil metode `display_table` dari kelas `View` untuk menampilkan hasil.

### Eksekusi Program

Program dieksekusi melalui blok berikut:

