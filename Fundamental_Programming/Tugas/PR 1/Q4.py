Question = str(input("What do you want to convert (USD or GBP) = "))

if Question == "USD":
    USD = float(input("USD = "))
    USD *= 0.65
    USD = str(USD)
    print(USD + " GBP")
elif Question == "GBP":
    GBP = float(input("GBP = "))
    GBP *= 100 / 65
    GBP = str(GBP)
    print(GBP + " USD")
else:
    print("I don't know about this currency")
    