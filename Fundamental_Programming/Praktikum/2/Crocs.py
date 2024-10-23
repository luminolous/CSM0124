def perkalianXor(n, number):
    xor = 1
    for i in range(n):
        for j in range(i+1,n):
            if number[i] != number[j]:
                xor *= number[i] ^ number[j]
            elif number[i] == number[j]:
                xor *= 0
                break
    print(xor)
    

n = int(input())
number = list(map(int, input().split()))
perkalianXor(n, number)
