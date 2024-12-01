# 0 0 0 0
# 0 1A 1B 0
# 0 1C 0 0 
# A : B, C
# B : A
# C : A
#indeks si A, B, C
# Berapa kursi yang sudah terduduki
# 4 - 1 = 3
# i = 1, j = 1
# Baris = 3, kolom = 4
# Jumlahin angka di arah mata angin setiap 1

N,M = map(int, input().split())
matrix = []

for i in range(N):
    masuk = list(map(str,input().split()))
    matrix.append(masuk)

# bari
# (1,1) baratnya adalah (1,0)
# (i,j) barat adalah (i, j - 1)
# (i,j) timur adalah (i, j + 1)
# (i,j) timur laut adalah (i - 1, j + 1)
# (i,j) barat laut adalah (i - 1, j - 1)
# (i,j) utaranya adalah (i - 1,j)
# (i,j) selatan adalah (i + 1, j)
# (i,j) tenggara  (i + 1, j + 1)
# (i,j) barat daya (i + 1, j - 1)

duduk = set()
for i in range(0,N):
    for j in range(0,M):
        if(i - 1 < 0 or i + 1 >= N or j - 1 < 0 or j + 1 >= M):
            continue
        if (matrix[i][j - 1] != 0 and j - 1 >= 0  ):
            duduk.add(matrix[i][j - 1])
        if(matrix[i][j + 1] != 0  and j + 1 < M ):
            duduk.add(matrix[i][j + 1])
        if(matrix[i - 1][j] !=0 and i - 1 >= 0):
            duduk.add(matrix[i- 1][j])
        if(matrix[i + 1][j] != 0 and i + 1 < N):
            duduk.add(matrix[i + 1][j])
        if(matrix[ i - 1][j + 1] !=0 and i - 1 >= 0 and j + 1 < M):
            duduk.add(matrix[ i - 1][j + 1])
        if(matrix[i - 1][j - 1] !=0 and i - 1 >= 0 and j - 1 >= 0):
            duduk.add(matrix[i - 1][j - 1])
        if(matrix[i + 1][j - 1] != 0 and i + 1 < N and j - 1 >= 0):
            duduk.add(matrix[i + 1][j - 1])
        if(matrix[i + 1][j + 1] != 0 and i + 1 < N and j + 1 < M):
            duduk.add(matrix[i + 1][j + 1])

duduk.remove('0')
print(len(duduk))
print(duduk)
