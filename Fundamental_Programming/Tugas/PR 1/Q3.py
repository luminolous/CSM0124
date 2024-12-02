hour, minute = input().split()

hour = int(hour)
minute = int(minute)

minute = minute / 60
time = hour + minute

temperature = (4 * (time ** 2)) / (time + 2)
temperature = temperature - 20

print("The Temperature is " + ("%.2f" %(temperature)) + " C")
