X, Y = map(int, map(int, input().split()))
x, y = map(int, map(int, input().split()))
M = int(input())
if (x == 0 and y == 0) or (x == 0 and y == Y) or (x == X and y == 0) or (x == X and y == Y):
    chance_to_out = 3
elif(x == 0) or (y == 0) or (x == X) or (y == Y):
    chance_to_out = 5
else:
    chance_to_out = 8

if M == 1:
    mx_1, my_1 = map(int, map(int, input().split()))
    makan = True
elif M == 2:
    mx_1, my_1 = map(int, map(int, input().split()))
    mx_2, my_2 = map(int, map(int, input().split()))
    makan = True
elif M == 3:
    mx_1, my_1 = map(int, input().split())
    mx_2, my_2 = map(int, input().split())
    mx_3, my_3 = map(int, input().split())
    if (x+1 == mx_1 or x-1 == mx_1) or (y+1 == my_1 or y-1 == my_1):
        chance_to_out -= 1
    if (x+1 == mx_2 or x-1 == mx_2) or (y+1 == my_2 or y-1 == my_2):
        chance_to_out -= 1
    if (x+1 == mx_3 or x-1 == mx_3) or (y+1 == my_3 or y-1 == my_3):
        chance_to_out -= 1
elif M == 4:
    mx_1, my_1 = map(int, input().split())
    mx_2, my_2 = map(int, input().split())
    mx_3, my_3 = map(int, input().split())
    mx_4, my_4 = map(int, input().split())
    if (x+1 == mx_1 or x-1 == mx_1) or (y+1 == my_1 or y-1 == my_1):
        chance_to_out -= 1
    if (x+1 == mx_2 or x-1 == mx_2) or (y+1 == my_2 or y-1 == my_2):
        chance_to_out -= 1
    if (x+1 == mx_3 or x-1 == mx_3) or (y+1 == my_3 or y-1 == my_3):
        chance_to_out -= 1
    if (x+1 == mx_4 or x-1 == mx_4) or (y+1 == my_4 or y-1 == my_4):
        chance_to_out -= 1
elif M == 5:
    mx_1, my_1 = map(int, input().split())
    mx_2, my_2 = map(int, input().split())
    mx_3, my_3 = map(int, input().split())
    mx_4, my_4 = map(int, input().split())
    mx_5, my_5 = map(int, input().split())
    if (x+1 == mx_1 or x-1 == mx_1) or (y+1 == my_1 or y-1 == my_1):
        chance_to_out -= 1
    if (x+1 == mx_2 or x-1 == mx_2) or (y+1 == my_2 or y-1 == my_2):
        chance_to_out -= 1
    if (x+1 == mx_3 or x-1 == mx_3) or (y+1 == my_3 or y-1 == my_3):
        chance_to_out -= 1
    if (x+1 == mx_4 or x-1 == mx_4) or (y+1 == my_4 or y-1 == my_4):
        chance_to_out -= 1
    if (x+1 == mx_5 or x-1 == mx_5) or (y+1 == my_5 or y-1 == my_5):
        chance_to_out -= 1
elif M == 6:
    mx_1, my_1 = map(int, input().split())
    mx_2, my_2 = map(int, input().split())
    mx_3, my_3 = map(int, input().split())
    mx_4, my_4 = map(int, input().split())
    mx_5, my_5 = map(int, input().split())
    mx_6, my_6 = map(int, input().split())
    if (x+1 == mx_1 or x-1 == mx_1) or (y+1 == my_1 or y-1 == my_1):
        chance_to_out -= 1
    if (x+1 == mx_2 or x-1 == mx_2) or (y+1 == my_2 or y-1 == my_2):
        chance_to_out -= 1
    if (x+1 == mx_3 or x-1 == mx_3) or (y+1 == my_3 or y-1 == my_3):
        chance_to_out -= 1
    if (x+1 == mx_4 or x-1 == mx_4) or (y+1 == my_4 or y-1 == my_4):
        chance_to_out -= 1
    if (x+1 == mx_5 or x-1 == mx_5) or (y+1 == my_5 or y-1 == my_5):
        chance_to_out -= 1
    if (x+1 == mx_6 or x-1 == mx_6) or (y+1 == my_6 or y-1 == my_6):
        chance_to_out -= 1
elif M == 7:
    mx_1, my_1 = map(int, input().split())
    mx_2, my_2 = map(int, input().split())
    mx_3, my_3 = map(int, input().split())
    mx_4, my_4 = map(int, input().split())
    mx_5, my_5 = map(int, input().split())
    mx_6, my_6 = map(int, input().split())
    mx_7, my_7 = map(int, input().split())
    if (x+1 == mx_1 or x-1 == mx_1)or (y+1 == my_1 or y-1 == my_1):
        chance_to_out -= 1
    if (x+1 == mx_2 or x-1 == mx_2)or (y+1 == my_2 or y-1 == my_2):
        chance_to_out -= 1
    if (x+1 == mx_3 or x-1 == mx_3)or (y+1 == my_3 or y-1 == my_3):
        chance_to_out -= 1
    if (x+1 == mx_4 or x-1 == mx_4)or (y+1 == my_4 or y-1 == my_4):
        chance_to_out -= 1
    if (x+1 == mx_5 or x-1 == mx_5)or (y+1 == my_5 or y-1 == my_5):
        chance_to_out -= 1
    if (x+1 == mx_6 or x-1 == mx_6)or (y+1 == my_6 or y-1 == my_6):
        chance_to_out -= 1
    if (x+1 == mx_7 or x-1 == mx_7)or (y+1 == my_7 or y-1 == my_7):
        chance_to_out -= 1
elif M == 8:
    mx_1, my_1 = map(int, input().split())
    mx_2, my_2 = map(int, input().split())
    mx_3, my_3 = map(int, input().split())
    mx_4, my_4 = map(int, input().split())
    mx_5, my_5 = map(int, input().split())
    mx_6, my_6 = map(int, input().split())
    mx_7, my_7 = map(int, input().split())
    mx_8, my_8 = map(int, input().split())
    if (x+1 == mx_1 or x-1 == mx_1) or (y+1 == my_1 or y-1 == my_1):
        chance_to_out -= 1
    if (x+1 == mx_2 or x-1 == mx_2) or (y+1 == my_2 or y-1 == my_2):
        chance_to_out -= 1
    if (x+1 == mx_3 or x-1 == mx_3) or (y+1 == my_3 or y-1 == my_3):
        chance_to_out -= 1
    if (x+1 == mx_4 or x-1 == mx_4) or (y+1 == my_4 or y-1 == my_4):
        chance_to_out -= 1
    if (x+1 == mx_5 or x-1 == mx_5) or (y+1 == my_5 or y-1 == my_5):
        chance_to_out -= 1
    if (x+1 == mx_6 or x-1 == mx_6) or (y+1 == my_6 or y-1 == my_6):
        chance_to_out -= 1
    if (x+1 == mx_7 or x-1 == mx_7) or (y+1 == my_7 or y-1 == my_7):
        chance_to_out -= 1
    if (x+1 == mx_8 or x-1 == mx_8) or (y+1 == my_8 or y-1 == my_8):
        chance_to_out -= 1
elif M == 0:
    chance_to_out = 0

#print(chance_to_out)
print('Senshi makan hari ini!') if chance_to_out > 0 else print('Senshi makannya besok aja deh.')
