list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
search = 11

def binser(list, search):
    if not list:
        return -1

    mid_index = len(list) // 2
    med = list[mid_index]

    print(f"Daftar: {list}, Median: {med}")

    if med == search:
        return mid_index
    
    elif search < med:
        return binser(list[:mid_index], search)
    
    else:
        result = binser(list[mid_index + 1:], search)

        if result != -1:
            return mid_index + 1 + result
        
        return -1 
    
print(binser(list, search))