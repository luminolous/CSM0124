# Cara 1
a, b = map(int, input().split())

if a % b == 0:
    c = b
    d = a
else:
    c = a
    d = b

hasil = (c + d)

print(hasil)

# Cara 2
a, b = map(int, input().split())

if a % b == 0:
    c = b
else:
    c = a

d = (a * b) // c

hasil = (c * d // a) + (c * d // b)

print(hasil)