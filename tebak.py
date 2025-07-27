import random

def main():
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    print("=== Game Tebak Angka ===")
    print("Saya sudah memilih angka 1–100.")
    print("Coba tebak!")

    while True:
        try:
            tebakan = int(input("Masukkan tebakanmu: "))
        except ValueError:
            print("Harus angka!")
            continue

        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu kecil!")
        elif tebakan > angka_rahasia:
            print("Terlalu besar!")
        else:
            print(f"Selamat! Benar dalam {percobaan} percobaan.")
            break

if __name__ == "__main__":
    main()
