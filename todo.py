# List kosong untuk menyimpan tugas
tasks = []

# Fungsi untuk menampilkan semua tugas
def show_tasks():
    # Jika daftar tugas kosong, beri tahu pengguna
    if not tasks:
        print("Tidak ada tugas.")
    else:
        # Jika ada tugas, tampilkan dengan penomoran
        print("\nDaftar Tugas:")
        for i, task in enumerate(tasks, start=1):
            # enumerate digunakan untuk menambahkan nomor secara otomatis mulai dari 1
            print(f"{i}. {task}")

# Fungsi untuk menambah tugas ke dalam list
def add_task():
    # Minta input tugas dari pengguna
    task = input("Masukkan tugas baru: ")
    # Tambahkan tugas ke list
    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

# Fungsi untuk menghapus tugas dari list
def delete_task():
    # Tampilkan daftar tugas terlebih dahulu agar user bisa memilih
    show_tasks()
    try:
        # Minta input nomor tugas yang ingin dihapus
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        # Hapus tugas sesuai nomor (dikurangi 1 karena index dimulai dari 0)
        tasks.pop(nomor - 1)
        print("Tugas berhasil dihapus!")
    except (ValueError, IndexError):
        # Tangani error jika input bukan angka atau nomor tidak valid
        print("Nomor tugas tidak valid!")

# Fungsi utama program
def main():
    while True:
        # Tampilkan menu utama
        print("\n=== To-Do List ===")
        print("1. Tampilkan tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. Keluar")

        # Minta input pilihan dari user
        pilihan = input("Pilih menu (1/2/3/4): ")

        # Logika menu
        if pilihan == "1":
            # Tampilkan daftar tugas
            show_tasks()
        elif pilihan == "2":
            # Tambahkan tugas baru
            add_task()
        elif pilihan == "3":
            # Hapus tugas yang dipilih user
            delete_task()
        elif pilihan == "4":
            # Keluar dari program
            print("Terima kasih! Program selesai.")
            break
        else:
            # Tangani jika user memasukkan input selain 1-4
            print("Pilihan tidak valid!")

# Menjalankan fungsi main() hanya jika file ini dijalankan langsung
if __name__ == "__main__":
    main()
