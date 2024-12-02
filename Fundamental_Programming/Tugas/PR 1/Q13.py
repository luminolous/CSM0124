enrolled = int(input("Enrolled student = "))

section = str(enrolled // 30) #fungsi dari tanda // adalah untuk pembagian dengan pembulatan ke bawah
studentleft = str(enrolled % 30) #fungsi dari tanda % adalah pembagian dengan mengitung sisa nya

print("The whole section = " + section)
print("The student left = " + studentleft)

