def solve_tower_level_elevation(N, M, K, tower_levels, cases):
    total_energy_needed = 0
    
    for start, end in cases:
        energy_needed = sum(tower_levels[start-1:end-1]) #  Menghitung jumlah energi yang dibutuhkan
        total_energy_needed = total_energy_needed + energy_needed
    
    if total_energy_needed <= M:
        remaining_energy = M - total_energy_needed
        return f"EZ banget, energiku sisa {remaining_energy}!"
    else:
        energy_shortage = total_energy_needed - M
        return f"NT, kurang {energy_shortage} energi sih."

# Bagian Input
N, M, K = map(int, input().split())
tower_levels = list(map(int, input().split()))
cases = [tuple(map(int, input().split())) for _ in range(K)]

# Result dan print
result = solve_tower_level_elevation(N, M, K, tower_levels, cases)
print(result)
