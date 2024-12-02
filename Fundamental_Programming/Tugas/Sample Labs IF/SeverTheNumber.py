x = int(input())
x = "%06d" %x
x = int(x)

if x < 0:
    x = x * (-1)

if x < -100000 or x > 100000:
    print("The number must in interval -100000 <= number <= 100000")
    quit()

a = x // 100000
an = x % 100000
b = an // 10000
bn = an % 10000
c = bn // 1000
cn = bn % 1000
d = cn // 100
dn = cn % 100
e = dn // 10
en = dn % 10
f = en // 1

if a == 4 or b == 4 or c == 4 or d == 4 or e == 4 or f == 4:
    print("SEVER")
else:
    print("UNITE")

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
