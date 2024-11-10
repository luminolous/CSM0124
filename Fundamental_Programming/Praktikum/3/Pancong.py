import sys
sys.setrecursionlimit(10 ** 9)
recSave = {}

def panc(n, recSave):
    if n in recSave:
        return recSave[n]
    else:
        if n == 0:
            return 0
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 1
        if n == 4:
            return 2
        else:
            recSave[n] = (panc(n-2, recSave) + panc(n-3, recSave) + panc(n-4, recSave)) % (10**9 + 7)
            return recSave[n]

print(panc(int(input()), recSave))