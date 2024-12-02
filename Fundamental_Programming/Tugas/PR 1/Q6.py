grade = input("Enter desired grade> ")
min = float(input("Enter minimum average required> "))
avg = float(input("Enter current average in course> "))
perc = float(input("Enter how much the final counts as a percentage of the course grade> "))

perc1 = 100 - perc
perc_avg = avg * perc1 / 100
fnl_crs = (min - perc_avg) * 100 / perc

print("You need a score of " + ("%.2f" %(fnl_crs)) + " on the final to get a " + grade)

