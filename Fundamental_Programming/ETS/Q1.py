m = int(input())

result = []
for _ in range(m):
    n = int(input())
    arr = list(map(int, input().split()))

    # if only has 1 number
    if len(arr) == 1:
        result.append('-1')

    # if has > 1 number with the same largest mode
    mort1 = []
    for num in set(arr):
        m = []
        for i in arr:
            if num == i:
                m.append(i)
        if len(m) > 1:
            mort1.append(m)

    mnum = 0
    for i in range(len(mort1)):
        mnum = max(mnum, len(mort1[i]))

    dcd = []
    for i in range(len(mort1)):
        if len(mort1[i]) == mnum:
            dcd.append(i)

    if len(dcd) > 1:
        value = 1
        for i in range(len(mort1)):
            value *= mort1[i][0]
        
        res = []
        for i in range(len(mort1)):
            if i == len(mort1) - 1:
                res.append(f'{mort1[i][0]} =' + f' {value}')
            else:
                res.append(f'{mort1[i][0]}' + '*')
        
        result.append(res)

    # if only have 1 number with the largest mode
    if len(mort1) == 1:
        rest = f'{mnum}' + ' * ' + f'{mort1[0][0]}' + ' = ' + f'{mnum * mort1[0][0]}'
        result.append(rest)

for i in result:
    for j in i:
        print(j, end="")
    if i == result[len(result) - 1]:
        quit()
    print('\n')