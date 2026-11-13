suhu_reaktor = int(input("masukkan suhu reaktor = "))
tekanan_gas = int(input("masukkan suhu tekanan gas = "))

if suhu_reaktor > 1000:
    if tekanan_gas > 50:
        print("MELTDOWN! SEGERA EVAKUASI!")
    else:
        print("Bahaya Suhu: Segera Turunkan Daya!")
elif suhu_reaktor > 500:
    if tekanan_gas > 30:
        print("Tekanan Tidak Stabil")
    else:
        print("Operasi Reaktor Normal")
else:
    print("Reaktor Belum Cukup Panas")
status = "pompa maksimal" if suhu_reaktor > 800 else "pompa normal"
print("status operasional = ", status)