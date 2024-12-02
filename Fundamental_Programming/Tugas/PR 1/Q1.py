print("TAXI FARE CALCULATOR")

x = float(input("Enter beginning odometer reading=> "))
y = float(input("Enter ending odometer reading=> "))

if x < y:
    z = (y - x)
    z1 = (float((z) * 1.50))
    print("You traveled distance of " + ("%.1f" %(z)) + " miles. At $1.50 per mile, your fare is $" + ("%.2f" %(z1)))

elif x == y:
    print("Go fix your car bro!")

else:
    print("Are you joking at me?")