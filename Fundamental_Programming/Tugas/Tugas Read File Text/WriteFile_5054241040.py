file = open("MyName.txt", "w") 

for i in range(3): 
    name = input("Enter nama: ") 
    file.write(name) 
    file.write("\n") 
    
file.close() 

print("Data is written into the file.\n")

file_f = open("MyFamily.txt", "w") 
FamilyList = []
for i in range(5): 
    name = input("Enter nama: ") 
    file_f.write(name) 
    file_f.write("\n") 
    
file_f.close() 

print("Data is written into the file.")