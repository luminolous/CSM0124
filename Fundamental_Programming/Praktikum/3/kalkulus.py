def f(n):
    if n % 2 == 0:
        return 1 + f(n//2)
    elif n == 1:
        return 1
    else:
        return 1 + f(n-1)

a = int(input())
print(f(a))
