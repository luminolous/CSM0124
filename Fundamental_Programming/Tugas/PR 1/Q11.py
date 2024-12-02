m, n = map(float,input("m and n = ").split())

side1 = (m**2) - (n**2)
side2 = 2 * m * n
hypotenuse = (m**2) + (n**2)

print("side1 = " + ("%.2f" %(side1)))
print("side2 = " + ("%.2f" %(side2)))
print("hypotenuse = " + ("%.2f" %(hypotenuse)))
