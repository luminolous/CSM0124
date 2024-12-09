def funct(x):
    return (-len(str(x)), x)
n = [4, 3, 5, 22, 333, 11]
n.sort(key=funct, reverse=False)
print(n)