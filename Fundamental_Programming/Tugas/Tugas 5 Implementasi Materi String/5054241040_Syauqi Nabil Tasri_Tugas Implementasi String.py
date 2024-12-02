string0 = 'Syauqi Nabil Tasri'
string1 = '5054241040'
string2 = 'Sumbar'

print(f'Nama saya adalah {string0}') #Menampilkan nama
print(f'NRP saya adalah {string1}') #Menampilkan NRP
print(f'Saya berasal dari {string2}') #Menampilkan Asal
print(f'Inisial saya adalah {string0[0]}{string0[7]}{string0[13]}') #Menampilkan Inisial
print(f'Nama belakang saya {string0[-5:]}') #Menampilkan nama belakang
print(f'Nama panggilan saya {string0[:6]}') #Menampilkan nama panggilan
print(f'Reverse dari NRP saya adalah {string1[::-1]}') #Reverse string

# Mengganti string
# Cara 1
string3 = 'Saya mahasiswa RKA'
list1 = list(string3)
list1[5:] = 'bukan mahasiswa RPL'
stringNama = ''.join(list1)
print(stringNama)
# Cara 2
stringRPL = string3[0:4] + ' bukan ' + string3[5:16] + 'PL'
print(stringRPL)

# Menghapus karakter
# Cara 1, memakai fungsi del
stringDelete = list(string2)
del stringDelete[1]
del stringDelete[3]
stringDel = ''.join(stringDelete)
print(stringDel)
# Cara 2, menghapus semua karakter yang akan dihapus dalam kalimat
stringAsalkota = 'Padang'
stringAsalkota = ''.join([i for i in stringAsalkota if i != 'a'])
print(stringAsalkota)

# Escape Sequencing in Python
# Menggunakan Triple Quotes
String02 = '''Nama saya Syauqi'''
print(f"{String02}")
# Print single quote atau double quote menggunakan Backslash
String01 = "Nama saya \"Syauqi\'"
print(f"{String01}")
# Mem-print backslash
String03 = "C:\\Syauqi\\040\\"
print(f"{String03}")
# Melakukan tab
String00 = "Hi\tI\'m Syauqi"
print(f"{String00}")
# Menambah new line
String04 = "Syauqi\n040"
print(f"{String04}")

# Menggunakan Octal
StringNamaInOctal = "\123\171\141\165\161\151"
print(f"\nNama saya adalah : {StringNamaInOctal}")
# Saat di print bilangan octal tidak di convert ke huruf
StringNumber = r"\110\145\154\154\157" 
print(f"Nama saya adalah : {StringNumber}")
# Menggunakan HEX
StringHEX = "Nama saya \x53\x79\x61\x75\x71\x69"
print(f'\n{StringHEX}')
# Bilangan HEX tidak di convert
StringWithoutHex = r"Nama saya \x53\x79\x61\x75\x71\x69"
print(f"{StringWithoutHex}")

# Python String Formatting
# Contoh 1
# Default order
StringD1 = "{} {} {}".format('Nama', 'saya', 'Syauqi')
print(f"\nDefault order: {StringD1}")

# Positional Formatting
StringD2 = "{1} {0} {2}".format('Nama', 'saya', 'Syauqi')
print(f"Positional order: {StringD2}")

# Keyword Formatting
StringD3 = "{c} {b} {a}".format(a='Nama', b='saya', c='Syauqi')
print(f"Order of Keywords: {StringD3}")

# contoh 2
# Formatting of Integers
StringF1 = "{0:b}".format(7)
print(f"\nBinary representation of 7 is {StringF1}")

# Formatting of Floats
StringF2 = "{0:e}".format(34.698)
print(f"Exponent representation of 34.698 is {StringF2}")

# Rounding off Integers
StringF3 = "{0:.1f}".format(1/5)
print(f"one-fifth is : {StringF3}")

# Contoh 3
# String alignment
String20 = "|{:<10}|{:^10}|{:>10}|".format(string0[:6],
                                          string1, 
                                          string2)
print(f"\n{String20}")

# To demonstrate aligning of spaces
String30 = "{0:^6} berasal dari {1:<5}".format(string0[:6],
                                                    string2)
print(String30)

# Contoh 4
Integer1 = 57/4
print('\nNilai integer dari 3.1f is %3.1f' % Integer1)
print('Nilai integer dari 3.2f is %3.2f' % Integer1)

