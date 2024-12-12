file1 = open(r"5054241040.txt", "w")
L = ["Nama Saya ...\n", "Saya berasal dari ...\n", "Saya suka ...\n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open(r"....txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(17) function is ")
print(file1.read(17))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(100))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()