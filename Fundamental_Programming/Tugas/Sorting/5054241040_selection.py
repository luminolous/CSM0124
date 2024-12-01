def selectionSort(vlue):
    n = len(vlue)
    for i in range(n):
        min_idx = i 
        for j in range(i+1, n):
            if vlue[j] < vlue[min_idx]:
                min_idx = j
        vlue[i], vlue[min_idx] = vlue[min_idx], vlue[i] 
    return vlue

vlue = [6, 3, 25, 12, 2, 1, 0]
print(selectionSort(vlue))
