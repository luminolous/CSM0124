population = int(input("Population = "))

toilet = (population / 3)
toilet = toilet + 0.5
print(toilet)
toilet = ("%.0f" %(toilet))
toilet = int(toilet)
print(toilet)

magn = 2 * 14 * toilet
cost = toilet * 150

magn1 = 15 * 14 * toilet
magn2 = magn1 - magn

magn = str(magn)
cost = str(cost)
magn2 = str(magn2)

print("Magnitude = " + magn + " liters/day")
print("Magnitude water saved = " + magn2 + "liters/day")
print("Cost = $" + cost)

