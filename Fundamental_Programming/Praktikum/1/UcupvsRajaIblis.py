hp = int(input())
knight = int(input())
minions = int(input())

ap_ucup = 100
hp_minions, ap_minions = 100, 2
hp_knight, ap_knight = 500, 5
hp_maou, ap_maou = 1000, 100

if minions > 0:
    hp_left_minions = hp - (minions // 2 * 2)
else:
    hp_left_minions = 0

if knight > 0:
    hp_left_knight = hp_left_minions - (knight // 2 * 5) * 5
else:
    hp_left_knight = hp_left_minions

hp_left = hp_left_knight - (10 * 100)

print(hp_left)

print(f'Yey! Ucup Menang! HP tersisa: {hp_left}') if hp_left > 0 else print('Yah! Ucup Meninggoy. ')