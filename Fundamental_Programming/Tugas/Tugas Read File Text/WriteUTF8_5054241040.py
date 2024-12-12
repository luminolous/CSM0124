file = open('Quotes_....txt', 'w', encoding='utf8')
for i in range(3): 
    quote = input("Enter your favorite quote : ") 
    file.write(quote) 
    file.write("\n") 
    
file.close() 