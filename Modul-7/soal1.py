tugas = {}

while True:
    print("\nTO DO LIST")
    print("1. Tambah Tugas")
    print("2. Tandai Tugas Selesai")
    print("3. Tampilkan Semua Tugas")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas Selesai dan Belum")
    print("6. Keluar")

    try:
        pilihan = int(input("Pilih menu: "))
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")
        continue
    

    if pilihan == 1:
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            print("Tugas sudah ada")
        else:
            tugas[nama] = "Belum Selesai"
            print("Tugas berhasil ditambahkan")

    elif pilihan == 2:
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil ditandai selesai")
        else:
            print("Tugas tidak ditemukan")

    elif pilihan == 3:
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            print("\nDAFTAR TUGAS")
            for nama, status in tugas.items():
                print(nama, ":", status)

    elif pilihan == 4:
        nama = input("Masukkan nama tugas: ")

        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus")
        else:
            print("Tugas tidak ditemukan")

    elif pilihan == 5:
        selesai = 0
        belum = 0

        for status in tugas.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum)

    elif pilihan == 6:
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
