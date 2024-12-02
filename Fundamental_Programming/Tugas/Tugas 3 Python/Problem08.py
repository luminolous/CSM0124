def solve_tower_level(M, tower_levels, cases):
    total_energy_needed = 0 # total_energy_needed = 0 supaya bisa dijumlahkan dengan energy needed di dalam looping dan nilainya bertambah seiring dengan bertambahnya energy_needed

    for case in cases:
        x, y = case # Digunakan untuk memecah nilai dari list nya menjadi 2 variable 
        energy_needed = sum(tower_levels[x-1:y-1]) # Menggunakan sum karena lebih simpel untuk menjumlahkan semua nilai list dan mengambil nilai dalam list sesuai dengan yang diminta menggunakan slicing
        total_energy_needed += energy_needed # Menjumlahkan energi yang telah didapat dengan energi yang tadi yang telah selesai dijumlahkan
    
    if total_energy_needed <= M: # Kondisi ketika player memenangkan game dengan energi tersisa >= 0
        remaining_energy = M - total_energy_needed
        return f"EZ banget, energiku sisa {remaining_energy}!"
    else: # Kondisi ketika player kalah dalam game dengan sisa energi < 0
        energy = total_energy_needed - M
        return f"NT, kurang {energy} energi sih."

# Inputan
while True: # Berfungsi untuk melakukan perulangan apabila ada yang tidak sesuai
    N, M, K = map(int, input().split()) # Inputan untuk jumlah lantai, total energi player, banyak baris dari x dan y 
    tower_levels = list(map(int, input().split())) # Banyak energi yang dibutuhkan pada setiap level dari setiap lantai
    if N != len(tower_levels): # Program meminta user apabila banyak level yang user input tidak sama dengan N
        print('Banyak level tidak sesuai dengan yang kamu inputkan, masukkan input yang benar!')
    else:
        cases = [] # Berisi nilai x dan y
        for i in range(K):
            case = list(map(int, input().split())) # Melakukan input untuk mengumpulkan data level mana saja yang akan dilalui player
            cases.append(case)
        # Result and print
        print(f"{solve_tower_level(M, tower_levels, cases)}")
        break

