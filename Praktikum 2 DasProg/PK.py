string = input()
n = len(string)

if n > 200 or n < 0:
        print('Bukan King!')
        quit()

result = []
for i in range(min(1,n),n):
    a = n-i
    if string[i-1] != string[a]:
        print('Bukan King!')
        quit()
print('Palindrome King!')
