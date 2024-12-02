# Problem 2
import numpy as np
total_input = int(input("masukkan berapa jumlah inputan: "))
arr_numbers = [0] * total_input

for i in range(total_input):
    numbers = int(input("masukkan angka: "))
    arr_numbers[i] = numbers

final_result = ""
for numbers in arr_numbers:
  binary = np.binary_repr(numbers, width=32)
  splitted_binary = [str(binary)[i:i+8] for i in range(0, len(str(binary)), 8)]

  result = ""
  for i in splitted_binary:
    decimal = int(i, 2)
    result += chr(decimal)
  final_result += result

print(final_result)