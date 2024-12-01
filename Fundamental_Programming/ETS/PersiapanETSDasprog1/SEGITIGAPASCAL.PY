def segitiga_pascal(n):
    # Membuat segitiga Pascal
    segitiga = []
    
    for i in range(n):
        baris = [1] * (i + 1)
        for j in range(1, i):
            baris[j] = segitiga[i-1][j-1] + segitiga[i-1][j]
        segitiga.append(baris)
    
    # Mencetak segitiga Pascal
    for baris in segitiga:
        print(' '.join(map(str, baris)).center(n * 2))

# Contoh penggunaan
n = int(input("Masukkan jumlah baris segitiga Pascal: "))
segitiga_pascal(n)

