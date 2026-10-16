pelanggan = 0



while True:
    beli = (input("masukkan tiket =  "))
    reguler = 40000
    vip = 75000
    vvip = 100000

    if reguler <= 40000 :
        print("mendapatkan harga  = ", reguler)
    elif vip <= 75000 :
        print("mendapatkan harga  = ", vip)
    else :
        print("mendapatkan harga  = " , vvip)

    pelanggan += 1

