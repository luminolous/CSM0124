list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14 ,15 ,16 ,17, 18, 19, 20]
search = 10

for i in range(0, (len(list)-1)):
    if list[i] != search:
        continue
    elif list[i] == search:
        print(f"Found {search} at index {i}")
        break
    else:
        print(f"Element {search} not found in the list")
        break