rows = int(input("Enter the number of rows: "))

triangle = [[1]]

for i in range(1, rows):
    row = [1]
    for j in range(1, i):
        row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)
    triangle.append(row)

max_width = len(' '.join(map(str, triangle[-1])))

for row in triangle:
    print(' '.join(map(str, row)).center(max_width)) 
