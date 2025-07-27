tasks = []

def show_tasks():
    if not tasks:
        print("Tidak ada tugas.")
    else:
        print("\nDaftar Tugas:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Masukkan tugas baru: ")
    tasks.append(task)
    print("Tugas berhasil ditambahkan!")

def delete_task():
    show_tasks()
    try:
        nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        tasks.pop(nomor - 1)
        print("Tugas berhasil dihapus!")
    except (ValueError, IndexError):
        print("Nomor tugas tidak valid!")

def main():
    while True:
        print("\n=== To-Do List ===")
        print("1. Tampilkan tugas")
        print("2. Tambah tugas")
        print("3. Hapus tugas")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            show_tasks()
        elif pilihan == "2":
            add_task()
        elif pilihan == "3":
            delete_task()
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
