s, n, m = map(int, input().split())
posisi = {}

for i in range(s):
    x = input()
    a, b = map(int, input().split())
    posisi[(a, b)] = x

banding = list(input().split())
sekitar = []

for x in banding:
    for (a,b), murid in posisi.items():
        if murid == x:
            if b > 0 and (a, b - 1) in posisi:
                sekitar.append(posisi[(a, b - 1)])
            if (a, b + 1) in posisi:
                sekitar.append(posisi[(a, b + 1)])
            if a > 0 and (a - 1, b) in posisi:
                sekitar.append(posisi[(a - 1, b)])
            if (a + 1, b) in posisi:
                sekitar.append(posisi[(a + 1, b)])

print(set(sekitar))