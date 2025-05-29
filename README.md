# 📚 Sistem Manajemen Data Mahasiswa

Sebuah aplikasi Python berbasis terminal untuk:

* Mengelola data mahasiswa
* Menghitung Fibonacci dan Permutasi secara rekursif
* Memvalidasi ekspresi kurung menggunakan struktur data stack

Cocok untuk pembelajaran konsep dasar struktur data dan rekursi dalam Python.

---

## ✨ Fitur Utama

### 1. Manajemen Data Mahasiswa

* Tambah data mahasiswa (NIM, Nama, Kelas, Nilai Tugas)
* Tampilkan seluruh data dalam format tabel

### 2. Fungsi Rekursif

* Hitung nilai ke-n dari deret Fibonacci
* Hitung nilai permutasi P(n, r)

### 3. Validasi Ekspresi Kurung

* Validasi ekspresi matematika yang mengandung kurung (), {}, dan \[]
* Menunjukkan jumlah dan kesesuaian pasangan kurung

---

## 💡 Konsep Algoritma

* **Rekursi:**

  * Digunakan untuk perhitungan Fibonacci dan Permutasi

* **Stack (LIFO):**

  * Validasi ekspresi kurung berdasarkan urutan buka-tutup

* **List of Dictionary:**

  * Menyimpan data mahasiswa

---

## 🔧 Cara Menjalankan Program

1. Pastikan Python 3.x sudah terinstal
2. Jalankan perintah berikut di terminal:

   ```bash
   python main.py
   ```

---

## 🔹 Navigasi Menu

```
MENU UTAMA
1. Manajemen Data Mahasiswa
2. Hitung Fibonacci (Rekursif)
3. Hitung Permutasi (Rekursif)
4. Validasi Kurung (Stack)
5. Keluar
```

---

## 📄 Contoh Output (Ringkasan)

### Manajemen Data:

```
NIM           Nama             Kelas           Nilai
5243151043    Jaka Perdana     PTIK - A 2024   100
```

### Fibonacci:

```
Masukkan nilai n: 7
Fibonacci ke-7 = 13
F(0) = 0, F(1) = 1, ..., F(7) = 13
```

### Permutasi:

```
Masukkan n = 10, r = 7
P(10,7) = 10! / 3! = 604800
```

### Validasi Kurung:

```
Ekspresi: a(a+b)+c(c+d)
Status: VALID
```

---

## ❌ Kendala yang Dihadapi

* Perlu validasi input agar program tidak crash saat salah input
* Perhitungan Fibonacci lambat untuk nilai besar karena belum pakai memoization
* Validasi kurung tidak menangani ekspresi kompleks bersarang dalam kondisi ekstrim

### ✅ Solusi yang Dilakukan:

* Menggunakan `try-except` untuk penanganan error input
* Menampilkan posisi kesalahan kurung
* Menjaga logika tetap sederhana dan terarah ke tujuan edukatif

---

## 👨‍💼 Pengembang

* **Nama:** Jaka Perdana
* **Kelas:** PTIK - A 2024
* **Universitas:** \[Isi sesuai institusi Anda]

---

## 🙌 Kontribusi

1. Fork repo ini
2. Buat branch baru (`fitur-baru`)
3. Commit perubahan (`git commit -m "Tambah fitur"`)
4. Push ke GitHub
5. Buat pull request

---

> Proyek ini dibuat untuk memenuhi tugas UTS Struktur Data dan sebagai sarana belajar praktik struktur data dengan Python.
