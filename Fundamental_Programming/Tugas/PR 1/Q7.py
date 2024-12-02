gallons = float(input("Gallons = "))
eff = float(input("Efficiency = "))
eff = eff / 100

BTUpGall = 5800000 / 42

BTUgall = gallons * BTUpGall
BTUril = BTUgall * eff

print("BTU : " + ("%.2f" %(BTUril)))
