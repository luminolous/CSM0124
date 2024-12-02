lYard, wYard = input("Length and width of yard (feet) = ").split()
lHouse, wHouse = input("Length and width of house (feet) = ").split()
lard = float(lYard)
ward = float(wYard)
louse = float(lHouse)
wouse = float(wHouse)
rate = 2

yard = lard * ward
house = louse * wouse

if yard > house:
    grass = yard - house
    time = grass / rate
    print("Time required for cut the grass : " + ("%.2f" %(time)) + " feet/sec")
elif yard == house:
    print("Your house don't have more space for grass")
else:
    print("I think you should stop to imaginating have a house")
        