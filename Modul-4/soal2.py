for i in range(1, 8):
    print("\nhari ke = ", i)
    harga_h = 100000
    print("harga perhari = ", harga_h)
    total_harga = harga_h * i
    print("harga total sebelum upah = ", total_harga)

    jam_lembur = int(input("masukkan jam lembur = "))
    if jam_lembur <= 3:
        harga = 25000
        print("harga lembur = ", jam_lembur * harga)
    elif jam_lembur == 4:
        harga = 25000
        print("harga lembur = ", jam_lembur * harga)
    elif jam_lembur == 6:
        harga = 200000
        print("harga lembur = ", harga)
    elif jam_lembur == 8:
        harga = 300000
        print("harga lembur = ", harga)
    else :
        print("jumlah lembur tidak sesuai yang ditentukan")

    shift_malam = int(input("masukkan shift malam = "))
    harga = 50000
    print("harga shift malam per hari = ", harga)
    harga_total = 50000 * shift_malam
    print("harga shift malam = ", harga_total)

print("total harga keseluruhan = ", total_harga + harga + harga_total)