def traffic_light(M, N, T):
    # Total waktu satu siklus lampu lalu lintas
    total_cycle_time = 85  # 20 detik merah + 5 detik kuning + 60 detik hijau
    green_light_time = 60   # Waktu lampu hijau dalam 1 siklus
    
    # Total mobil di depan dan diri Anda
    total_cars = M + 1      # +1 karena kita termasuk mobil yang dihitung
    
    # Hitung sisa waktu dari lampu hijau yang aktif selama T detik
    full_cycles = T // total_cycle_time   # Berapa banyak siklus penuh?
    remaining_time = T % total_cycle_time # Sisa waktu di luar siklus penuh
    
    # Total waktu lampu hijau dalam siklus penuh
    effective_green_time = full_cycles * green_light_time
    
    # Hitung tambahan waktu hijau dari sisa waktu jika ada di rentang lampu hijau
    if remaining_time > 25:  # 20 detik merah + 5 detik kuning = 25 detik
        effective_green_time += remaining_time - 25
    
    # Hitung berapa mobil yang bisa lewat
    cars_passed = effective_green_time // 5  # 1 mobil bisa lewat per 5 detik hijau
    
    # Tentukan hasil akhir
    if cars_passed >= total_cars:
        print("YES!", 0)
    else:
        cars_left = total_cars - cars_passed
        print("NO!", cars_left)

# Input
M, N, T = map(int, input().split())
traffic_light(M, N, T)
