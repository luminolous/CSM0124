t = int(input())
m = []
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    q = int(input())
    
    current_sum = sum(arr[:k])
    min_sum = current_sum
    max_sum = current_sum
    
    for h in range(1, k+1):
        current_sum = sum(arr[:h])
        min_sum = min(min_sum, current_sum)
        max_sum = max(max_sum, current_sum)
        for i in range(1, n - h + 1):
            current_sum = current_sum - arr[i - 1] + arr[i + h - 1]
            min_sum = min(min_sum, current_sum)
            max_sum = max(max_sum, current_sum)

    if q == 1:
        m.append(max_sum)
    if q == 2:
        m.append(min_sum)

for i in m:
    print(i)
