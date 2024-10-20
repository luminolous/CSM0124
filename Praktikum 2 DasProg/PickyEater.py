n = int(input())
arr = list(map(int, input().split()))

if len(arr) == 1:
    print('0')
    quit()

list = []
for i in set(arr):
    mods = []
    for j in arr:
        if i == j:
            mods.append(i)
    if len(mods) > 1:
        list.append(mods)

maxnum = 0
for i in list:
    maxnum = max(maxnum, len(i))

num = []
for i in list:
    if len(i) == maxnum:
        num.append(i[0])

if len(num) > 1:
    print('-1')
    quit()

if len(num) == 1:
    print(num[0])
    print(len(arr) - len(list[0]))


