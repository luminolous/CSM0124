def mergeSort(vlue):
    if len(vlue) > 1:
        mid = len(vlue) // 2 
        left = vlue[:mid]
        right = vlue[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                vlue[k] = left[i]
                i += 1
            else:
                vlue[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            vlue[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            vlue[k] = right[j]
            j += 1
            k += 1
    return vlue

vlue = [64, 34, 25, 12, 22, 11, 90]
print(mergeSort(vlue))
