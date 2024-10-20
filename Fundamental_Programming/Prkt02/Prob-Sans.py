n = int(input())
arr = list(map(int, input().split()))

length = len(arr)
modus = []

for i in range(length):
        for j in range(length):
            if i != j and i < j:
                if arr[i] == arr[j]:
                    modus.append(arr[i])

a = set(modus)
modusNumber = []
for i in a:
    modusNumber.append(i)

print(f'modus : {max(modusNumber)}')

for i in range(2, max(modusNumber)):
     a = max(modusNumber) % i
     if a == 0:
          print('Yah, modusnya gak prima!')
          quit()
print('Wah, modusnya prima nih!')