h = int(input("height(m) = "))
v = int(input("the flow of water(m/s) = "))
g = 9.80
p = 1000

M = v * p
P = M * g * h
PE = P * 0.9
PMW = PE / 10**6
PMW = str(PMW)

print("The power(megawatts) is " + PMW)
