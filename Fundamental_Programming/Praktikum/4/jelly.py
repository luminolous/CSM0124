def searchIndex(num):
    count = 0
    for i in str(num):
        count += int(i)
    if len(str(count)) == 1:
        return count
    else:
        return searchIndex(count)

arr = list(map(int, input().split()))
index = []
for angka in arr:
    index.append(searchIndex(angka)) 
Arr = list(zip(arr, index))
Arr.sort(key=lambda item: (item[1], item[0]))
print(" ".join(str(isi[0]) for isi in Arr))