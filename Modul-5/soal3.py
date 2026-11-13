def nilai(nama, tugas, uts, uas):
    total_nilai = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

    if total_nilai > 85:
        grade = "A"
        status = "lulus"
    elif total_nilai > 70:
        grade = "B"
        status = "lulus"
    elif total_nilai > 55:
        grade = "C"
        status = "lulus"
    else:
        grade = "D"
        status = "tidak lulus"
    return f"Nama: {nama}, Total Nilai: {total_nilai}, Grade: {grade}, Status: {status}"

nama = input("Masukkan nama: ")
tugas = int(input("Masukkan nilai tugas: "))
uts = int(input("Masukkan nilai UTS: "))
uas = int(input("Masukkan nilai UAS: "))

print(nilai(nama, tugas, uts, uas))