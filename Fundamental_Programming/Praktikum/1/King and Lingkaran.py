x0, y0 = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

if x0 < -(10 ** 25) and x0 > (10 ** 25):
    print('No')
    quit()
if y0 < -(10 ** 25) and y0 > (10 ** 25):
    print('No')
    quit()
if x1 < -(10 ** 25) and x1 > (10 ** 25):
    print('No')
    quit()
if y1 < -(10 ** 25) and y1 > (10 ** 25):
    print('No')
    quit()
if x2 < -(10 ** 25) and x2 > (10 ** 25):
    print('No')
    quit()
if y2 < -(10 ** 25) and y2 > (10 ** 25):
    print('No')
    quit()

jarak_titik_pusat_ke_tujuan_raja = (((x0 - x2) ** 2) + ((y0 - y2) ** 2))

jarak_raja_ke_tujuan_raja = (((x1 - x2) ** 2) + ((y1 - y2) ** 2))

if jarak_titik_pusat_ke_tujuan_raja > jarak_raja_ke_tujuan_raja:
    print('Yes')
elif jarak_titik_pusat_ke_tujuan_raja < jarak_raja_ke_tujuan_raja:
    print('No')
else:
    print('No')
