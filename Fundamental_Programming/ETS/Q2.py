n, m = map(int, input().split())
arr = []
for _ in range(n):
    map = input().split()
    arr.append(map)

bomb = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == '0':
            if j-1 >= 0:
                    if arr[i][j-1] == '1':
                        bomb.append('a')
            if j + 1 != m:
                    if arr[i][j+1] == '1':
                        bomb.append('a')
            if i + 1 != n:
                    if arr[i+1][j] == '1':
                        bomb.append('a')
            if i-1 >= 0:
                    if arr[i-1][j] == '1':
                        bomb.append('a')
            if j-1 >= 0 and i + 1 != n:
                    if arr[i+1][j-1] == '1':
                        bomb.append('a')
            if j + 1 != m and i + 1 != n:
                    if arr[i+1][j+1] == '1':
                        bomb.append('a')
            if j-1 >= 0 and i-1 >= 0:
                    if arr[i-1][j-1] == '1':
                        bomb.append('a')
            if j + 1 != m and i-1 >= 0:
                    if arr[i-1][j+1] == '1':
                        bomb.append('a')
print(len(bomb))
