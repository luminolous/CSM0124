def can_B_jump(distances):
    # Nilai pertama adalah jarak maksimum lompatan n
    n = distances[0]
    # Sisanya adalah jarak antar pilar
    for distance in distances[1:]:
        if distance > n:
            print("NO HE CAN'T")
            return
    print("YES HE CAN")

distances = list(map(int, input().split())) 

can_B_jump(distances)
