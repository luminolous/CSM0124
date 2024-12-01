def cek_jalan(baris, kolom, batas_b, batas_k):
    if baris < 0 or kolom < 0:
        return False
    if baris >= batas_b or kolom >= batas_k:
        return False
    return True

def jalan(baris, kolom, peta, sudah_lewat, batas_b, batas_k, rute, sisa):
    # Cek apakah bisa jalan
    if not cek_jalan(baris, kolom, batas_b, batas_k):
        return False
    if peta[baris][kolom] == '1':
        return False
    if sudah_lewat[baris][kolom]:
        return False

    sudah_lewat[baris][kolom] = True
    rute.append((baris, kolom))

    if peta[baris][kolom] == '2':
        sisa[0] = sisa[0] - 1

    if baris == batas_b-1 and kolom == batas_k-1 and sisa[0] == 0:
        return True

    if jalan(baris+1, kolom, peta, sudah_lewat, batas_b, batas_k, rute, sisa):
        return True
    if jalan(baris, kolom+1, peta, sudah_lewat, batas_b, batas_k, rute, sisa):
        return True
    if jalan(baris, kolom-1, peta, sudah_lewat, batas_b, batas_k, rute, sisa):
        return True
    if jalan(baris-1, kolom, peta, sudah_lewat, batas_b, batas_k, rute, sisa):
        return True
    
    # Mundur kalau tidak ketemu jalan
    sudah_lewat[baris][kolom] = False
    rute.pop()
    if peta[baris][kolom] == '2':
        sisa[0] = sisa[0] + 1
    return False

def hitung_barang(peta, batas_b, batas_k):
    total = 0
    for i in range(batas_b):
        for j in range(batas_k):
            if peta[i][j] == '2':
                total = total + 1
    return total

kolom, baris = input().split()
kolom = int(kolom)
baris = int(baris)

peta = []
for i in range(baris):
    peta.append(list(input()))

sudah_lewat = []
for i in range(baris):
    baris_baru = []
    for j in range(kolom):
        baris_baru.append(False)
    sudah_lewat.append(baris_baru)

rute = []
sisa = [hitung_barang(peta, baris, kolom)]

ketemu = jalan(0, 0, peta, sudah_lewat, baris, kolom, rute, sisa)

if ketemu:
    hasil = []
    for i in range(baris):
        baris_hasil = []
        for j in range(kolom):
            baris_hasil.append(peta[i][j])
        hasil.append(baris_hasil)
    
    for b, k in rute:
        if hasil[b][k] != '1':
            hasil[b][k] = '*'
    
    for baris_hasil in hasil:
        print(''.join(baris_hasil))