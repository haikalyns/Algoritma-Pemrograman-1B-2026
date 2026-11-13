n = int(input("masukkan nilai = "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")



    print(" " * (2 * (n - i) + 5), end="")



    for j in range(1, i + 1):
        print(j % 10, end="")

    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()
