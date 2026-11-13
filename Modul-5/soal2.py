def palindrom(teks):
    teks = teks.lower().replace(" ", "")
    return teks == teks[::-1]

kata = input("Masukkan kata: ")

if palindrom(kata):
    print(f"{kata} adalah palindrom")
else:
    print(f"{kata} bukan palindrom")