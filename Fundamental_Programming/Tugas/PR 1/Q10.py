xpoint1, ypoint1 = map(float,input().split(','))
xpoint2, ypoint2 = map(float,input().split(','))

m = (ypoint2 - ypoint1) / (xpoint2 - xpoint1)
xmid = (xpoint2 + xpoint1) / 2
ymid = (ypoint2 + ypoint1) / 2
m1 = -1 / m
yi = ymid - m1 * xmid
m1 = str(m1)
yi = str(yi)
print("y = " + m1 + "x + " + yi)
