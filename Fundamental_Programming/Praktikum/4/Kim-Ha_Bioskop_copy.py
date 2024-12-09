
def binary_search(array, y):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] < y:
            low = mid + 1
        else:
            high = mid - 1
    return low

M, N = map(int, input().split())
array = []
for _ in range(N):
    array.extend(list(map(int, input().split())))
m = int(input())
target = []
x = list(map(int, input().split()))
target.extend(x)
array.sort()

for i in target:
    print(binary_search(array, i), end=" ")       