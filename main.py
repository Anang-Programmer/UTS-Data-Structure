"""
======================================================
        PROGRAM UTS STRUKTUR DATA (PYTHON)
        Nama      : Jaka Perdana
        NIM       : 5243151043
        Kelas     : PTIK - A
        Dosen     : Rosma Siregar S.Kom., M.Kom
======================================================

Deskripsi:
Program ini dibuat untuk memenuhi tugas UTS mata kuliah Struktur Data.
Program mencakup implementasi struktur data array, class (record), stack,
serta penggunaan fungsi rekursif untuk menyelesaikan beberapa masalah umum.

Fitur-fitur Utama:
1. Pengelolaan Data Mahasiswa:
   - Menyimpan data mahasiswa (nama, NIM, nilai) dalam bentuk class.
   - Menampilkan data mahasiswa.
   - Mencari mahasiswa berdasarkan NIM.

2. Fungsi Rekursif:
   - Menghitung deret Fibonacci secara rekursif.
   - Menghitung faktorial dari suatu angka.
   - Menghitung jumlah permutasi dari n dan r.

3. Stack:
   - Implementasi stack dengan array.
   - Validasi ekspresi kurung menggunakan prinsip LIFO.

Struktur Data yang Digunakan:
- Array/List: Untuk menyimpan banyak elemen data.
- Record/Class: Representasi struktur data mahasiswa.
- Stack: Struktur LIFO untuk validasi ekspresi.
- Rekursi: Untuk menyelesaikan perhitungan matematis berulang.

Catatan Tambahan:
- Program ini ditulis menggunakan bahasa Python 3.13
- Dilengkapi dengan menu interaktif untuk memudahkan pengguna.
- Penanganan error ditambahkan agar program lebih stabil.
- Validasi input disertakan untuk beberapa fungsi rekursif.
- Performa fungsi rekursif seperti Fibonacci menurun untuk input besar.

Penggunaan:
Jalankan program, lalu pilih menu yang tersedia sesuai kebutuhan Anda.
Tekan 0 untuk keluar dari program.

======================================================
"""

# 1. MANAJEMEN DATA MAHASISWA (Array dan Record)
class Mahasiswa:
    """
    Class untuk merepresentasikan data mahasiswa
    """
    data_mahasiswa = []
    
    def __init__(self, nim, nama, kelas, nilai_tugas):
        self.nim = nim
        self.nama = nama
        self.kelas = kelas
        self.nilai_tugas = nilai_tugas
    
    @classmethod
    def tambah_mahasiswa(cls, nim, nama, kelas, nilai_tugas):
        """
        Fungsi untuk menambahkan data mahasiswa ke dalam array
        """
        # Validasi input
        if not nim or not nama or not kelas:
            print("Error: NIM, Nama, dan Kelas tidak boleh kosong!")
            return False
        
        if not isinstance(nilai_tugas, int) or nilai_tugas < 0 or nilai_tugas > 100:
            print("Error: Nilai tugas harus berupa integer antara 0-100!")
            return False
        
        # Cek duplikasi NIM
        for mhs in cls.data_mahasiswa:
            if mhs.nim == nim:
                print(f"Error: NIM {nim} sudah terdaftar!")
                return False
        
        mhs = Mahasiswa(nim, nama, kelas, nilai_tugas)
        cls.data_mahasiswa.append(mhs)
        print(f"Mahasiswa {nama} berhasil ditambahkan!")
        return True
    
    @classmethod
    def tampilkan_mahasiswa(cls):
        """
        Fungsi untuk menampilkan seluruh data mahasiswa
        """
        if not cls.data_mahasiswa:
            print("=" * 50)
            print("TIDAK ADA DATA MAHASISWA")
            print("=" * 50)
            return
        
        print("=" * 70)
        print(f"{'No':<3} {'NIM':<12} {'Nama':<20} {'Kelas':<8} {'Nilai':<5}")
        print("=" * 70)
        
        for i, mhs in enumerate(cls.data_mahasiswa, 1):
            print(f"{i:<3} {mhs.nim:<12} {mhs.nama:<20} {mhs.kelas:<8} {mhs.nilai_tugas:<5}")
        
        print("=" * 70)
        print(f"Total Mahasiswa: {len(cls.data_mahasiswa)}")

# 2. FUNGSI REKURSIF (Fibonacci dan Permutasi)
def fibonacci_rekursif(n):
    """
    Fungsi rekursif untuk mencari nilai ke-n dari deret Fibonacci
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        raise ValueError("Input harus bilangan non-negatif!")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)

def faktorial_rekursif(n):
    """
    Fungsi rekursif untuk menghitung faktorial
    """
    if n < 0:
        raise ValueError("Input harus bilangan non-negatif!")
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial_rekursif(n - 1)

def permutasi_rekursif(n, r):
    """
    Fungsi rekursif untuk menghitung permutasi nPr = n!/(n-r)!
    """
    if n < 0 or r < 0:
        raise ValueError("Input harus bilangan non-negatif!")
    
    if r > n:
        return 0
    
    if r == 0:
        return 1
    
    return faktorial_rekursif(n) // faktorial_rekursif(n - r)

# 3. STACK UNTUK VALIDASI EKSPRESI
class Stack:
    """
    Implementasi Stack menggunakan list
    """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop dari stack kosong!")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek dari stack kosong!")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

def cek_validitas_kurung(ekspresi):
    """
    Fungsi untuk mengecek validitas tanda kurung dalam ekspresi
    Menggunakan stack untuk memastikan setiap kurung buka memiliki pasangan kurung tutup
    """
    stack = Stack()
    pasangan_kurung = {')': '(', ']': '[', '}': '{'}
    kurung_buka = '([{'
    kurung_tutup = ')]}'
    
    for i, char in enumerate(ekspresi):
        if char in kurung_buka:
            stack.push(char)
        elif char in kurung_tutup:
            if stack.is_empty():
                return False, f"Kurung tutup '{char}' di posisi {i} tidak memiliki pasangan"
            
            kurung_terakhir = stack.pop()
            if kurung_terakhir != pasangan_kurung[char]:
                return False, f"Kurung tidak sesuai: '{kurung_terakhir}' dengan '{char}' di posisi {i}"
    
    if not stack.is_empty():
        return False, f"Terdapat {stack.size()} kurung buka yang tidak memiliki pasangan"
    
    return True, "Ekspresi valid"

# ===================================================================
# FUNGSI INPUT DAN MENU
# ===================================================================

def input_data_mahasiswa():
    """
    Fungsi untuk input data mahasiswa dari pengguna
    """
    print("\n--- INPUT DATA MAHASISWA ---")
    try:
        nim = input("Masukkan NIM: ").strip()
        nama = input("Masukkan Nama: ").strip()
        kelas = input("Masukkan Kelas: ").strip()
        nilai_tugas = int(input("Masukkan Nilai Tugas (0-100): "))
        
        Mahasiswa.tambah_mahasiswa(nim, nama, kelas, nilai_tugas)
    except ValueError:
        print("Error: Nilai tugas harus berupa angka!")
    except Exception as e:
        print(f"Error: {e}")

def input_fibonacci():
    """
    Fungsi untuk input dan menghitung Fibonacci
    """
    print("\n--- HITUNG FIBONACCI ---")
    try:
        n = int(input("Masukkan nilai n untuk Fibonacci ke-n: "))
        
        if n < 0:
            print("Error: Input harus bilangan non-negatif!")
            return
        
        # Tampilkan peringatan untuk n besar
        if n > 35:
            konfirmasi = input(f"Perhitungan Fibonacci ke-{n} akan memakan waktu lama. Lanjutkan? (y/n): ")
            if konfirmasi.lower() != 'y':
                return
        
        hasil = fibonacci_rekursif(n)
        print(f"\nHasil: Fibonacci ke-{n} = {hasil}")
        
        # Tampilkan beberapa nilai sebelumnya jika diinginkan
        if n <= 20:
            tampilkan = input("Tampilkan deret Fibonacci dari 0 sampai n? (y/n): ")
            if tampilkan.lower() == 'y':
                print(f"\nDeret Fibonacci dari F(0) sampai F({n}):")
                for i in range(n + 1):
                    fib_val = fibonacci_rekursif(i)
                    print(f"F({i:2d}) = {fib_val:3d}")
                    
    except ValueError:
        print("Error: Input harus berupa angka!")
    except Exception as e:
        print(f"Error: {e}")

def input_permutasi():
    """
    Fungsi untuk input dan menghitung Permutasi
    """
    print("\n--- HITUNG PERMUTASI ---")
    try:
        n = int(input("Masukkan nilai n: "))
        r = int(input("Masukkan nilai r: "))
        
        hasil = permutasi_rekursif(n, r)
        
        print(f"\nHasil: P({n},{r}) = {n}!/({n}-{r})! = {hasil}")
        
        # Tampilkan detail perhitungan
        detail = input("Tampilkan detail perhitungan? (y/n): ")
        if detail.lower() == 'y':
            if n >= 0 and r >= 0 and r <= n:
                faktorial_n = faktorial_rekursif(n)
                faktorial_n_r = faktorial_rekursif(n - r)
                print(f"\nDetail perhitungan:")
                print(f"{n}! = {faktorial_n}")
                print(f"({n}-{r})! = {n-r}! = {faktorial_n_r}")
                print(f"P({n},{r}) = {faktorial_n} / {faktorial_n_r} = {hasil}")
                
    except ValueError:
        print("Error: Input harus berupa angka!")
    except Exception as e:
        print(f"Error: {e}")

def input_validasi_kurung():
    """
    Fungsi untuk input dan validasi ekspresi kurung
    """
    print("\n--- VALIDASI KURUNG ---")
    print("Masukkan ekspresi yang ingin divalidasi kurungnya.")
    print("Contoh: ((a+b)*c), {[a+(b*c)]}, (a+b))(")
    
    ekspresi = input("Masukkan ekspresi: ")
    
    print(f"\nMenganalisis ekspresi: '{ekspresi}'")
    
    valid, pesan = cek_validitas_kurung(ekspresi)
    
    if valid:
        print("✓ VALID:", pesan)
    else:
        print("✗ TIDAK VALID:", pesan)
    
    # Hitung dan tampilkan detail kurung
    kurung_count = {'(': 0, ')': 0, '[': 0, ']': 0, '{': 0, '}': 0}
    for char in ekspresi:
        if char in kurung_count:
            kurung_count[char] += 1
    
    print("\nDetail kurung dalam ekspresi:")
    print(f"  Kurung biasa    : '(' = {kurung_count['(']}, ')' = {kurung_count[')']}")
    print(f"  Kurung siku     : '[' = {kurung_count['[']}, ']' = {kurung_count[']']}")
    print(f"  Kurung kurawal  : '{{' = {kurung_count['{']}, '}}' = {kurung_count['}']}")

def menu_mahasiswa():
    """
    Sub-menu untuk manajemen data mahasiswa
    """
    while True:
        print("\n" + "=" * 50)
        print("MENU MANAJEMEN DATA MAHASISWA")
        print("=" * 50)
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data Mahasiswa")
        print("3. Kembali ke Menu Utama")
        print("=" * 50)
        
        pilihan = input("Pilih menu (1-3): ").strip()
        
        if pilihan == '1':
            input_data_mahasiswa()
        elif pilihan == '2':
            print("\n--- DATA MAHASISWA ---")
            Mahasiswa.tampilkan_mahasiswa()
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-3.")

def menu_utama():
    """
    Menu utama program
    """
    print("SELAMAT DATANG DI SISTEM MANAJEMEN DATA MAHASISWA")
    print("Dengan Fungsi Rekursif dan Validasi Stack")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 60)
        print("MENU UTAMA")
        print("=" * 60)
        print("1. Manajemen Data Mahasiswa")
        print("2. Hitung Fibonacci (Rekursif)")
        print("3. Hitung Permutasi (Rekursif)")
        print("4. Validasi Kurung (Stack)")
        print("5. Keluar")
        print("=" * 60)
        
        try:
            pilihan = input("Pilih menu (1-5): ").strip()
            
            if pilihan == '1':
                menu_mahasiswa()
            elif pilihan == '2':
                input_fibonacci()
            elif pilihan == '3':
                input_permutasi()
            elif pilihan == '4':
                input_validasi_kurung()
            elif pilihan == '5':
                print("\nTerima kasih telah menggunakan program ini!")
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid! Silakan pilih 1-5.")
                
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"Error: {e}")

# ===================================================================
# JALANKAN PROGRAM
# ===================================================================

if __name__ == "__main__":
    menu_utama()