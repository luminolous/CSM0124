from bisect import bisect_left

def search_optimized(flat_list, target):
    result = []
    for t in target:
        value = bisect_left(flat_list, t)
        result.append(str(value))
    return result

def printed(numberList, target):
    flat_list = sorted([num for row in numberList for num in row])
    result = search_optimized(flat_list, target)
    print(" ".join(result))

def inputed():
    size = list(map(int, input().split()))
    numberList = []
    for _ in range(size[0]):
        numberList.append(list(map(int, input().split())))
    m = int(input())
    target = list(map(int, input().split()))
    printed(numberList, target)

if __name__ == '__main__':
    inputed()
