import math
 
def jumpSearch( list , search , n ):
    step = math.sqrt(n)
    prev = 0
    while list[int(min(step, n)-1)] < search:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while list[int(prev)] < search:
        prev += 1
        if prev == min(step, n):
            return -1
    if list[int(prev)] == search:
        return prev
    return -1
 
list = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
search = 55
n = len(list)
print(jumpSearch(list, search, n))