belanja = int(input("masukkan belanja = "))
if belanja >= 200000 :
    diskon = belanja * 0.10
    total_diskon = belanja - diskon
    print("mendapatkan diskon 10% =", total_diskon, "rupiah")
elif belanja % 100000 == 0:
    diskon = belanja * 1.00
    total_diskon = belanja - diskon 
    print("mendapatkan diskon 100% = gratis", total_diskon, "rupiah")
elif belanja % 50000 == 0:
    diskon = belanja * 0.50
    total_diskon = belanja - diskon
    print("mendapatkan diskon 50% =", total_diskon, "rupiah")
elif belanja % 10000 == 0:
    diskon = belanja * 0.10
    total_diskon = belanja - diskon
    print("mendapatkan diskon 10% =", total_diskon, "rupiah")
else:
    total_diskon = belanja
    print("harga normal =", belanja, "rupiah")
cetak = "point bertambah" if total_diskon > 0 else "tidak ada point"
print("point keanggotaan = ",cetak)