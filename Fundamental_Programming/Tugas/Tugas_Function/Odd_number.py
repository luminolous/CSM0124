def odd(num):
    return len([i for i in num if i % 2 != 0])
print(odd(num = list(map(int, input('Enter numbers : ').split()))))