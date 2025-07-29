# Mengimpor modul random untuk menghasilkan angka acak
import random

# Fungsi utama program
def main():
    # Menghasilkan angka rahasia secara acak antara 1 hingga 100
    angka_rahasia = random.randint(1, 100)
    
    # Variabel untuk menghitung jumlah percobaan
    percobaan = 0

    # Menampilkan judul permainan dan instruksi awal
    print("=== Game Tebak Angka ===")
    print("Saya sudah memilih angka 1–100.")
    print("Coba tebak!")

    # Perulangan utama permainan
    while True:
        try:
            # Minta input dari pengguna dan ubah menjadi integer
            tebakan = int(input("Masukkan tebakanmu: "))
        except ValueError:
            # Jika input bukan angka, tampilkan peringatan dan ulangi
            print("Harus angka!")
            continue  # Melanjutkan ke awal perulangan

        # Menambah jumlah percobaan setiap kali user menebak
        percobaan += 1

        # Mengecek apakah tebakan terlalu kecil
        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        # Mengecek apakah tebakan terlalu besar
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        # Jika tebakan sama dengan angka rahasia
        else:
            # Menampilkan pesan kemenangan dan jumlah percobaan
            print(f"Selamat! Benar dalam {percobaan} percobaan.")
            break  # Keluar dari perulangan karena tebakan sudah benar

# Menjalankan fungsi main hanya jika file ini dijalankan langsung (bukan diimpor)
if __name__ == "__main__":
    main()
