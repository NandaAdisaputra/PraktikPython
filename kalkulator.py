# Fungsi untuk melakukan operasi penjumlahan
def tambah(a, b):
    # Mengembalikan hasil penjumlahan dari a dan b
    return a + b

# Fungsi untuk melakukan operasi pengurangan
def kurang(a, b):
    # Mengembalikan hasil pengurangan dari a dikurangi b
    return a - b

# Fungsi untuk melakukan operasi perkalian
def kali(a, b):
    # Mengembalikan hasil perkalian antara a dan b
    return a * b

# Fungsi untuk melakukan operasi pembagian
def bagi(a, b):
    # Memeriksa apakah nilai b adalah 0 karena pembagian dengan nol tidak valid
    if b == 0:
        # Jika b adalah 0, kembalikan pesan error
        return "Error: Tidak bisa dibagi nol!"
    # Jika b tidak 0, kembalikan hasil pembagian a dengan b
    return a / b

# Fungsi utama program
def main():
    # Menampilkan judul kalkulator
    print("=== Kalkulator Sederhana ===")

    try:
        # Menerima input angka pertama dari pengguna dan mengkonversinya ke tipe data float
        angka1 = float(input("Masukkan angka pertama: "))
        # Menerima input angka kedua dari pengguna dan mengkonversinya ke tipe data float
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        # Jika terjadi error saat konversi (misalnya input bukan angka), tampilkan pesan error
        print("Input harus angka!")
        return  # Keluar dari fungsi main jika input tidak valid

    # Menampilkan pilihan operasi yang dapat dilakukan
    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    
    # Menerima input pilihan operasi dari pengguna
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    # Menggunakan percabangan if-elif-else untuk menentukan operasi berdasarkan input pengguna
    if pilihan == "1":
        # Jika pilihan adalah "1", lakukan operasi penjumlahan
        hasil = tambah(angka1, angka2)
    elif pilihan == "2":
        # Jika pilihan adalah "2", lakukan operasi pengurangan
        hasil = kurang(angka1, angka2)
    elif pilihan == "3":
        # Jika pilihan adalah "3", lakukan operasi perkalian
        hasil = kali(angka1, angka2)
    elif pilihan == "4":
        # Jika pilihan adalah "4", lakukan operasi pembagian
        hasil = bagi(angka1, angka2)
    else:
        # Jika pilihan tidak sesuai dengan opsi yang tersedia, tampilkan pesan error
        print("Pilihan tidak valid!")
        return  # Keluar dari fungsi main karena pilihan tidak valid

    # Menampilkan hasil dari operasi yang telah dipilih
    print(f"Hasil: {hasil}")

# Memastikan bahwa fungsi main() hanya akan dijalankan ketika file ini dijalankan secara langsung
if __name__ == "__main__":
    main()
