jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
jumlah_lampu = int(input("Masukkan jumlah lampu setiap baris: "))

for nomor_baris in range(1, jumlah_baris + 1):
    print("Baris ke =", nomor_baris)

    for nomor_lampu in range(1, jumlah_lampu + 1):
        if nomor_lampu % 3 == 0:
            print(f"Lampu {nomor_lampu}: mengalami gangguan")
        else:
            print(f"Lampu {nomor_lampu}: berfungsi normal")

print("Periksa sumber listrik utama taman")