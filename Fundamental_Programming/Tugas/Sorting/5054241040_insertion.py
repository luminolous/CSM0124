def insertionSort(vlue):
    for i in range(1, len(vlue)):
        key = vlue[i]
        j = i - 1
        while j >= 0 and key < vlue[j]:
            vlue[j + 1] = vlue[j]
            j -= 1
        vlue[j + 1] = key
    return vlue

vlue = [6, 5, 4, 3, 2, 1, 9]
print(insertionSort(vlue))
