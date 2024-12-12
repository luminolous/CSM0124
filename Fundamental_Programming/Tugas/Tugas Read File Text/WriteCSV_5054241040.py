import csv

with open('chocolate.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Nama Merek Coklat", "Jenis Coklat", "Harga"])
    writer.writerow(["Delfi", "Dark Chocolate", 30000])
    writer.writerow(["SilverQueen", "Milk Chocolate", 10000])
    writer.writerow(["Toblerone", "White Chocolate", 20000])
    writer.writerow(["Cadbury", "Milk Chocolate", 10000])
    writer.writerow(["Hershey's", "Dark Chocolate", 12000])