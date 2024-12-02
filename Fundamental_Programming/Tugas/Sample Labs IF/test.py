# x = 1 // 3600
# print(x)

# X = 12
# X = "%02d" %X
# print(X)

# masukan = input()
# digit = len(masukan)
# hasil = 0
# for i in range(0, digit):
#     hasil = hasil + int(masukan[i]) ** digit
# print(digit)
# print(hasil)
# if int(masukan) == hasil:
#     print("This is armstrong")
# else:
#     print("This is not armstrong")    

def is_prime(number):
    if number <= 1:
        return False  # Bilangan kurang dari atau sama dengan 1 bukan prima
    for i in range(2, int(number) - 1):
        if number % i == 0:
            return False  # Jika bisa dibagi, bukan prima
    return True  # Jika tidak ada pembagi, maka prima

num = int(input("Masukkan sebuah bilangan: "))

if is_prime(num):
    print(f"{num} adalah bilangan prima")
else:
    print(f"{num} bukan bilangan prima")
