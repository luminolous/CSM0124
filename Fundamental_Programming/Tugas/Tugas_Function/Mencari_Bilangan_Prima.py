def prime(modusNumber):
    if modusNumber == 1:
        print('Gak Prima!')
        quit()

    for i in range(2, modusNumber):
        a = modusNumber % i
        if a == 0:
            print('Gak Prima!')
            quit()

    print('Prima!')

prime(int(input()))
