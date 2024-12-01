N, r, c = map(int,input().split())
acuan = list(map(str,input().split()))

#Membuat matrix r kali c (baris kali kolom) dengan semua nilainya sama dengan nol
matrix = [['0' for _ in range(c)] for _ in range(r)]

#Memasukan orang ke posisi yang ada di matrix, nama orang, k = baris ke berapa, l = kolom ke berapa
for i in range(N):
    nama_orang = input()
    k, l = map(int,input().split()) 
    matrix[k][l] = nama_orang

#Deklarasi array kosong "tempat_duduk" untuk menyimpan nilai siapa di samping siapa
tempat_duduk = [] 

#Looping untuk ngecek 
for m in range (0, r):
    for n in range(0, c):
        for orang in acuan:
            if matrix[m][n] == orang:
                if n - 1 >= 0:
                    if matrix[m][(n - 1)] != '0':
                        tempat_duduk.append(matrix[m][(n - 1)])
                if n + 1 < c:
                    if matrix[m][(n + 1)] != '0':
                        tempat_duduk.append(matrix[m][(n + 1)])
                if m - 1 >= 0:
                    if matrix[(m - 1)][n] != '0':
                        tempat_duduk.append(matrix[(m - 1)][n])
                if m + 1 < r:
                    if matrix[(m + 1)][n] != '0':
                        tempat_duduk.append(matrix[(m + 1)][n])

#Ngeprint buat siapa aja orangnya dan jumlah orangnya
print(set(tempat_duduk))
print(f"jumlah orang : {len(set(tempat_duduk))}")