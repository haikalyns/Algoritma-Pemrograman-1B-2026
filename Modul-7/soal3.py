daftar_undangan = set()
peserta_a = set()
peserta_b = set()


while True:
    nama = input("Masukkan nama daftar undangan (ketik '0' untuk berhenti): ")
    if nama == "0":
        break
    daftar_undangan.add(nama)

while True:
    nama = input("Masukkan nama peserta webinar A (ketik '0' untuk berhenti): ")
    if nama == "0":
        break
    peserta_a.add(nama)

while True:
    nama = input("Masukkan nama peserta webinar B (ketik '0' untuk berhenti): ")
    if nama == "0":
        break
    peserta_b.add(nama)


print("\nDaftar Undangan:", daftar_undangan)
print("Peserta Webinar A:", peserta_a) 
print("Peserta Webinar B:", peserta_b)


print("\nsemua peserta", peserta_a | peserta_b)
print("peserta Webinar keduanya", peserta_a & peserta_b)
print("peserta Webinar A yang tidak ikut di Webinar B", peserta_a - peserta_b)
print("peserta Webinar B yang tidak ikut di Webinar A", peserta_b - peserta_a)
print("peserta yang tidak hadir", daftar_undangan - (peserta_a | peserta_b))