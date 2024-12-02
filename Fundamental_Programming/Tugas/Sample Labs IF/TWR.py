def cat_jump(lst, b, c, indices):
    # Lakukan loncatan sebanyak 'c' kali
    for _ in range(c):
        # Ambil 'b' elemen terakhir dan pindahkan ke depan
        lst = lst[-b:] + lst[:-b]
    
    # Ambil nilai dari tiga indeks yang diminta
    result = [lst[i] for i in indices]
    
    return result

lst = [1, 2, 3, 4, 5, 6, 7]  # Daftar awal
b = 7  # Jumlah elemen yang meloncat dari belakang ke depan
c = 3  # Jumlah loncatan
indices = [0, 3, 5]  # Indeks yang diminta (0, 3, 5)

output = cat_jump(lst, b, c, indices)
print(*output)  # Cetak hasilnya
