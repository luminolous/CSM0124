def search(arr, y):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < y:
            low = mid + 1
        else:
            high = mid - 1
    return low

size = list(map(int, input().split()))
numberList = []
for i in range(size[1]):
    numberList.extend(list(map(int, input().split())))
numberList = sorted(numberList)
m = int(input())
target = list(map(int, input().split()))
search(numberList, target)