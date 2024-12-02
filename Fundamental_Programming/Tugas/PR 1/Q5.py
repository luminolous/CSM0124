volume = float(input("Volume to be infused (ml) = "))
minute = float(input("Minutes over which to infused = "))

minute = minute / 60
#minute = float("%.1f" %(minute))
print(minute)
rate = volume / minute

print("VTBI: " + ("%.2f" %(volume)) + " ml")
print("Rate: " + ("%.2f" %(rate)) + " ml/hr")
