import csv

with open('chocolate.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"{header[0]:<20} {header[1]:<20} {header[2]:<10}")
    for row in reader:
        if int(row[2]) > 15000:
            print(f"{row[0]:<20} {row[1]:<20} {row[2]:<10}")