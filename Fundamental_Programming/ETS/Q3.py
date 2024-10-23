n = int(input())

print('+' + ('-' * ((n*2)+1)) + '+')

for i in range(n):
    for j in range(n):
        if j == 0:
            print('| ', end='')
        if i % 2 == 0:
            if j % 2 == 0:
                    print('v ', end='')
            else:
                    print('. ', end='')
            if j == n-1:
                    print('| ', end='')
        else:
            if j % 2 == 0:
                    print('. ', end='')
            else:
                    print('v ', end='')
            if j == n-1:
                    print('|', end='')
    print()    

print('+' + ('-' * ((n*2)+1)) + '+')