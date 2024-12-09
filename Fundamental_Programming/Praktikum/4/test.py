# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# search = 11
# def binser(list, search):
#     if not list:
#         return -1

#     mid_index = len(list) // 2
#     med = list[mid_index]

#     print(f"Daftar: {list}, Median: {med}")

#     if med == search:
#         return mid_index

#     if list[0] < list[len(list) - 1]:
#         if search < med:
#             return binser(list[:mid_index], search)
#         else:
#             result = binser(list[mid_index + 1:], search)
#             if result != -1:
#                 return mid_index + 1 + result
#             return -1

#     if list[0] > list[len(list) - 1]:
#         if search > med:
#             return binser(list[:mid_index], search)
#         else:
#             result = binser(list[mid_index + 1:], search)
#             if result != -1:
#                 return mid_index + 1 + result
#             return -1

# print(binser(list, search))

def f(k, a, b, n):
    return (k // a) * (b // a) >= n
def binser(a, b, n):
    l = 1
    r = 100000
    while r - l > 1:
        mid = (l + r) // 2
        if f(mid, a, b, n):
            r = mid
        else:
            l = mid + 1
    if f(l, a, b, n):
        return l
    else:
        return r

# def merge(arr, left, mid, right):
#     n1 = mid - left + 1
#     n2 = right - mid
 
#     L = [0] * n1
#     R = [0] * n2
 
#     for i in range(n1):
#         L[i] = arr[left + i]
#     for j in range(n2):
#         R[j] = arr[mid + 1 + j]
 
#     i = 0
#     j = 0
#     k = left
 
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
 
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
 
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
 
# def merge_sort(arr, left, right):
#     if left < right:
#         mid = (left + right) // 2
 
#         merge_sort(arr, left, mid)
#         merge_sort(arr, mid + 1, right)
#         merge(arr, left, mid, right)
 
# def print_list(arr):
#     for i in arr:
#         print(i, end=" ")
#     print()
 
# if __name__ == "__main__":
 
#     #  TODO : Implementasikan kode program disini