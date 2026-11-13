daftar = []

while True:
    peserta = input("Masukkan nama peserta (ketik selesai untuk berhenti): ")

    if peserta == "selesai":
        break

    daftar.append(peserta)

print("\nPemeriksaan nama peserta:")

for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

penyusup = input("\nMasukkan nama yang dicurigai: ")

if penyusup in daftar:
    daftar.remove(penyusup)
    print("Nama berhasil dihapus")
else:
    print("Nama tidak ditemukan")

print("\nDaftar peserta akhir:", daftar)