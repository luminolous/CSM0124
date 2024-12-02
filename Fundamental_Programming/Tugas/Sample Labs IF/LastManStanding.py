def last_man_standing(N, C):
    # Jika N % 4 == 0, pemain yang memulai akan kalah
    if N % 4 == 0:
        # Jika C = 1 (Lala memulai), maka Lili menang
        # Jika C = 2 (Lili memulai), maka Lala menang
        if C == 1:
            return "Lala"
        elif C == 2:
            return "Lili"
        
    else:
        # Jika N % 4 != 0, pemain yang memulai akan menang
        return "Lala" if C == 1 else "Lili"

# Contoh Input
N, C = map(int, input().split())

# Output Pemenang
print(last_man_standing(N, C))
