asisten = []

while True:
    nama = input("Masukkan nama asisten (cukup untuk berhenti): ")

    if nama == "cukup":
        break

    asisten.append(nama)

asisten_awal = tuple(asisten)

tambahan = input("Masukkan asisten tambahan: ")

asisten_akhir = asisten_awal + (tambahan,)

hari = []

while True:
    nama_hari = input("Masukkan hari tugas (cukup untuk berhenti): ")

    if nama_hari == "cukup":
        break

    hari.append(nama_hari)

hari_tugas = tuple(hari)

pengecualian_asisten = input("Masukkan nama asisten pengecualian: ")
pengecualian_hari = input("Masukkan hari pengecualian: ")

print("\nJadwal Shift:")

for nama in asisten_akhir:
    for h in hari_tugas:
        if nama == pengecualian_asisten and h == pengecualian_hari:
            continue

        print(nama, "=", h)