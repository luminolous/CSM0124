def is_prime(number):
    if number <= 1:
        return False  # Bilangan kurang dari atau sama dengan 1 bukan prima
    for i in range(2, int(number) - 1):
        if number % i == 0:
            return False  # Jika bisa dibagi, bukan prima
    return True  # Jika tidak ada pembagi, maka prima

number = int(input())

if is_prime(number):
    print("IT IS A PRIME")
else:
    print("IT IS NOT A PRIME")
