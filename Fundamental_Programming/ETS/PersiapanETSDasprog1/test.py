# print('hello',end=" ")
# print('world')

# m, n = map(int, input().split())

# for i in range(m):
#     for j in range(n):
#         if i % 2 == 0:
#             if j % 2 == 0:
#                 print('*', end='')
#             else:
#                 print('#',end='')
#         else:
#             if j % 2 == 0:
#                 print('#',end='')
#             else:
#                 print('*',end='')
#     print()

r = 5
x = 1
for i in range(r):
    for j in range(i+1):
        print(x, end=' ')
    x+=2
    print()
    