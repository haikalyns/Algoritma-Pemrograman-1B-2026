playlist = {}

while True:
    print("\nPLAYLIST MUSIK")
    print("1. Membuat playlist")
    print("2. Menambahkan lagu ke playlist")
    print("3. Menampilkan semua playlist dan lagu")
    print("4. Mencari lagu")
    print("5. Menghapus lagu dari playlist")
    print("6. Menghapus playlist")
    print("7. Keluar")

    while True:
        try:
            pilihan = int(input("Pilih menu: "))
            break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    if pilihan == 1:
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            print("Playlist sudah ada")
        else:
            playlist[nama_playlist] = {}
            print("Playlist berhasil dibuat")

    elif pilihan == 2:
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama_playlist][judul] = penyanyi
            print("Lagu berhasil ditambahkan ke playlist")
        else:
            print("Playlist tidak ditemukan")

    elif pilihan == 3:
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            print("\nDAFTAR PLAYLIST")

            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)

                if len(lagu) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print(judul, "-", penyanyi)

    elif pilihan == 4:
        lagu_dicari = input("Masukkan judul lagu yang dicari: ")

        for nama, lagu in playlist.items():
            if lagu_dicari in lagu:
                print(f"Lagu '{lagu_dicari}' ditemukan di playlist '{nama}'")
                print("Penyanyi:", lagu[lagu_dicari])
                break
        else:
            print(f"Lagu '{lagu_dicari}' tidak ditemukan di semua playlist")

    elif pilihan == 5:
        nama_playlist = input("Masukkan nama playlist: ")

        if nama_playlist in playlist:
            judul = input("Masukkan judul lagu yang ingin dihapus: ")

            if judul in playlist[nama_playlist]:
                del playlist[nama_playlist][judul]
                print("Lagu berhasil dihapus dari playlist")
            else:
                print("Lagu tidak ditemukan di playlist")
        else:
            print("Playlist tidak ditemukan")

    elif pilihan == 6:
        nama_playlist = input("Masukkan nama playlist yang ingin dihapus: ")

        if nama_playlist in playlist:
            del playlist[nama_playlist]
            print("Playlist berhasil dihapus")
        else:
            print("Playlist tidak ditemukan")

    elif pilihan == 7:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")