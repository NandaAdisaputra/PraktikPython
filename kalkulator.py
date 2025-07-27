def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Tidak bisa dibagi nol!"
    return a / b

def main():
    print("=== Kalkulator Sederhana ===")

    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input harus angka!")
        return

    print("\nPilih operasi:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == "1":
        hasil = tambah(angka1, angka2)
    elif pilihan == "2":
        hasil = kurang(angka1, angka2)
    elif pilihan == "3":
        hasil = kali(angka1, angka2)
    elif pilihan == "4":
        hasil = bagi(angka1, angka2)
    else:
        print("Pilihan tidak valid!")
        return

    print(f"Hasil: {hasil}")

if __name__ == "__main__":
    main()
