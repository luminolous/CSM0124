x = int(input())

if x >= 0:
    x = x % 2
    if x == 1:
        print("ho")
    elif x == 0:
        print("hi")
elif x < 0:
    x = x % 2
    if x == 1:
        print("he")
    elif x == 0:
        print("ha")

