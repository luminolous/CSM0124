def bubbleSort(value):
    n = len(value)
    for i in range(n):
        for j in range(0, n-i-1):
            if value[j] > value[j+1]:
                value[j], value[j+1] = value[j+1], value[j]
    return value

value = [64, 4, 25, 2, 22, 11, 9]
print(bubbleSort(value))
