kamera = {
    "Canon": (150000, 3),
    "Nikon": (125000, 2),
    "Sony": (200000, 2),
    "Fujifilm": (250000, 1)
}

daftar_sewa = []
riwayat_sewa = []
pelanggan = set()
akun_user = {
    "admin" : "12345678"
}
nomor_sewa = 1


def login():
    while True:
        print("\nLOGIN SISTEM PENYEWAAN KAMERA")
        print("1. Login")
        print("2. Register")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")


        if pilihan == "1":
            print("\nLOGIN")
            username = input("Username: ")
            password = input("Password: ")

            if username in akun_user and akun_user[username] == password:
                print(f"\nLogin {username} berhasil!")
                return username
            else:
                print("\nUsername atau password salah!")

        elif pilihan == "2":
            print("\nREGISTER AKUN")
            user = input("Masukkan username: ")
            pwd = input("Masukkan password: ")

            if user == "" or pwd == "":
                print("Username dan password tidak boleh kosong!")
                continue

            if user.lower() == "admin":
                print("Username admin tidak boleh digunakan!")
                continue

            if user in akun_user:
                print("Username sudah digunakan!")
                continue

            akun_user[user] = pwd
            print("\nRegistrasi berhasil! Silakan login.")


        elif pilihan == "0":
            print("\nTerima kasih telah menggunakan sistem!")
            return "keluar"

        else:
            print("\nPilihan tidak tersedia!")


def tampilkan_kamera():
    print("\nDAFTAR KAMERA")

    if len(kamera) == 0:
        print("Belum ada kamera.")
        return

    for nama, data in kamera.items():
        harga, stok = data

        print(f"Nama  : {nama}")
        print(f"Harga : Rp{harga:,}/hari")
        print(f"Stok  : {stok} unit")
        print("-" * 30)


def tambah_kamera():
    print("\nTAMBAH KAMERA")

    nama = input("Nama kamera: ")

    if nama == "":
        print("Nama kamera tidak boleh kosong!")
        return

    if nama in kamera:
        print("Kamera sudah tersedia!")
        return

    try:
        harga = int(input("Harga sewa per hari: "))
        stok = int(input("Jumlah stok kamera: "))

        if harga <= 0 or stok <= 0:
            print("Harga dan stok harus lebih dari 0!")
            return

    except ValueError:
        print("Input harus berupa angka!")
        return

    kamera[nama] = (harga, stok)
    print("Kamera berhasil ditambahkan!")


def update():
    tampilkan_kamera()

    nama = input("Nama kamera yang ingin di update: ")

    if nama not in kamera:
        print("Kamera tidak ditemukan!")
        return

    harga, stok = kamera[nama]

    print("\nDATA KAMERA SAAT INI")
    print(f"Nama  : {nama}")
    print(f"Harga : Rp{harga:,}")
    print(f"Stok  : {stok}")

    print("\nMASUKKAN DATA BARU")

    nama_baru = input("Nama kamera baru: ")

    if nama_baru == "":
        print("Nama kamera tidak boleh kosong!")
        return

    if nama_baru != nama and nama_baru in kamera:
        print("Nama kamera sudah digunakan!")
        return

    try:
        harga_baru = int(input("Harga kamera baru: "))
        stok_baru = int(input("Stok kamera baru: "))

        if harga_baru <= 0 or stok_baru < 0:
            print("Harga harus lebih dari 0 dan stok tidak boleh negatif!")
            return

    except ValueError:
        print("Input harus berupa angka!")
        return

    del kamera[nama]

    kamera[nama_baru] = (harga_baru, stok_baru)

    print("\nData kamera berhasil diperbarui!")


def hapus_kamera():
    tampilkan_kamera()

    nama = input("Nama kamera yang ingin dihapus: ")

    if nama not in kamera:
        print("Kamera tidak ditemukan!")
        return

    for data in daftar_sewa:
        if data["kamera"] == nama:
            print("Kamera sedang disewa dan tidak bisa dihapus!")
            return

    del kamera[nama]

    print("Kamera berhasil dihapus!")


def sewa_kamera(username):
    global nomor_sewa

    tampilkan_kamera()

    nama = username

    nama_kamera = input("Pilih kamera: ")

    if nama_kamera not in kamera:
        print("Kamera tidak ditemukan!")
        return

    harga, stok = kamera[nama_kamera]

    if stok <= 0:
        print("Maaf, kamera sedang tidak tersedia!")
        return

    try:
        hari = int(input("Lama sewa (hari): "))

        if hari <= 0:
            print("Lama sewa harus lebih dari 0!")
            return

    except ValueError:
        print("Input harus berupa bilangan bulat!")
        return

    total = harga * hari

    print("\nRINCIAN PENYEWAAN")
    print(f"Nama pelanggan: {nama}")
    print(f"Nama kamera   : {nama_kamera}")
    print(f"Lama sewa     : {hari} hari")
    print(f"Harga per hari: Rp{harga:,}")
    print(f"Total biaya   : Rp{total:,}")

    konfirmasi = input("Lanjutkan penyewaan? (y/n): ").lower()

    if konfirmasi == "y":
        data_sewa = {
            "id": nomor_sewa,
            "nama": nama,
            "kamera": nama_kamera,
            "hari": hari,
            "total": total
        }

        daftar_sewa.append(data_sewa)
        riwayat_sewa.append(data_sewa.copy())

        kamera[nama_kamera] = (harga, stok - 1)
        pelanggan.add(nama)

        print("\nPenyewaan berhasil!")
        print(f"Nomor transaksi: {nomor_sewa}")

        nomor_sewa += 1

    else:
        print("Penyewaan dibatalkan.")


def tampilkan_sewa(username=None):
    print("\nDAFTAR PENYEWAAN")

    if username is None:
        data_tampil = daftar_sewa
    else:
        data_tampil = [
            data for data in daftar_sewa
            if data["nama"] == username
        ]

    if len(data_tampil) == 0:
        print("Belum ada data penyewaan.")
        return

    for data in data_tampil:
        print(f"Nomor transaksi : {data['id']}")
        print(f"Nama pelanggan  : {data['nama']}")
        print(f"Kamera          : {data['kamera']}")
        print(f"Lama sewa       : {data['hari']} hari")
        print(f"Total biaya     : Rp{data['total']:,}")
        print("-" * 30)


def kembalikan_kamera(username):
    tampilkan_sewa(username)

    data_milik_user = [
        data for data in daftar_sewa
        if data["nama"] == username
    ]

    if len(data_milik_user) == 0:
        return

    try:
        nomor = int(input("Masukkan nomor transaksi: "))

    except ValueError:
        print("Nomor transaksi harus berupa angka!")
        return

    for data in daftar_sewa:
        if data["id"] == nomor and data["nama"] == username:
            nama_kamera = data["kamera"]

            harga, stok = kamera[nama_kamera]
            kamera[nama_kamera] = (harga, stok + 1)

            daftar_sewa.remove(data)

            print("Kamera berhasil dikembalikan!")
            return

    print("Nomor transaksi tidak ditemukan!")


def laporan():
    print("\nLAPORAN PENYEWAAN")

    total_pendapatan = 0

    for data in riwayat_sewa:
        total_pendapatan += data["total"]

    print(f"Jumlah transaksi aktif : {len(daftar_sewa)}")
    print(f"Jumlah transaksi total: {len(riwayat_sewa)}")
    print(f"Jumlah pelanggan unik  : {len(pelanggan)}")
    print(f"Total pendapatan       : Rp{total_pendapatan:,}")


def menu_admin():
    while True:
        print("\nMENU ADMIN")
        print("1. Tampilkan daftar kamera")
        print("2. Tambah kamera")
        print("3. Update kamera")
        print("4. Hapus kamera")
        print("5. Lihat daftar penyewaan")
        print("6. Laporan penyewaan")
        print("7. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kamera()

        elif pilihan == "2":
            tambah_kamera()

        elif pilihan == "3":
            update()

        elif pilihan == "4":
            hapus_kamera()

        elif pilihan == "5":
            tampilkan_sewa()

        elif pilihan == "6":
            laporan()

        elif pilihan == "7":
            print("Admin berhasil logout!")
            break

        else:
            print("Pilihan tidak tersedia!")


def menu_penyewa(username):
    while True:
        print(f"\nMENU USER - {username}")
        print("1. Tampilkan daftar kamera")
        print("2. Sewa kamera")
        print("3. Lihat daftar penyewaan")
        print("4. Kembalikan kamera")
        print("5. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_kamera()

        elif pilihan == "2":
            sewa_kamera(username)

        elif pilihan == "3":
            tampilkan_sewa(username)

        elif pilihan == "4":
            kembalikan_kamera(username)

        elif pilihan == "5":
            print(f" {username} berhasil logout!")
            break

        else:
            print("Pilihan tidak tersedia!")

while True:
    role = login()

    if role == "admin":
        print("Masuk ke menu admin")
        menu_admin()

    elif role == "keluar":
        print("Program selesai.")
        break

    elif role is not None:
        print(f"Masuk ke menu user: {role}")
        menu_penyewa(role)