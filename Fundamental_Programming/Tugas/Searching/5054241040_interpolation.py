def interpolationSearch(arr, lo, hi, x):
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo]))
        if arr[pos] == x:
            return pos
        elif arr[pos] < x:
            return interpolationSearch(arr, pos + 1, hi, x)
        elif arr[pos] > x:
            return interpolationSearch(arr, lo, pos - 1, x)
    return -1
 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = len(arr)
x = 18
print(interpolationSearch(arr, 0, n - 1, x))