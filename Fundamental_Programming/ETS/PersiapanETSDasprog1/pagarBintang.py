m, n = map(int, input().split())

for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                print('*', end='')
            else:
                print('#', end='')
        else:
            if j % 2 == 0:
                print('#', end='')
            else:
                print('*', end='')
    print()
