# for i in range(5):
#     print("Hello")

# a = 'append'
# a.append('20')
# print(a)

# a = [1,2,3]

# for i in range(1,3):
#     print(a[i])

# cases = [list(map(int, input().split()))]

# for case in cases:
#     start, end = case
#     print(start)
#     print(end)

# case = [1,1,2]
# print(case[0:0])
# print(set(case))

# case = input().strip()
# print(case)

# case = ord('A')
# print(case)

# char = 'A'
# if char.isupper():
#     print('upper')
# elif char.islower():
#     print('lower') 

# case = list(input().split())
# case = ' '.join(case)
# # case = case.split(',')
# print(case)
# print(len(case))

# case = list(input().split())
# word = ''
# for i in range(len(case)):
#     word += case[i] + ' '
# print(word)
# print(len(word))
# if case.isalpha():
#     print('true')\

# case = input().strip()
# print(case)
# print(len(case))

# while True:
#     a = 10
#     case = int(input())
#     if a != case:
#         print('coba lagi')

room_x, room_y = map(int, input().split())
senshi_x, senshi_y = map(int, input().split())
monsters = int(input())

if monsters == 0:
    print('Senshi makan hari ini!')

if monsters >= 1:
    first_monster_x, first_monster_y = map(int, input().split())
    if monsters >= 2:
            second_monster_x, second_monster_y = map(int, input().split())
            if monsters >= 3:
                third_monster_x, third_monster_y = map(int, input().split())
                if monsters >= 4:
                    fourth_monster_x, fourth_monster_y = map(int, input().split())
                    if monsters >= 5:
                        fifth_monster_x, fifth_monster_y = map(int, input().split())
                        if monsters >= 6:
                            sixth_monster_x, sixth_monster_y = map(int, input().split())
                            if monsters >= 7:
                                seventh_monster_x, seventh_monster_y = map(int, input().split())
                                if monsters == 8:
                                    eighth_monster_x, eighth_monster_y = map(int, input().split())

# kekanan
senshi_x += 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()
# kekanan
senshi_x -= 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()
# kekanan
senshi_y += 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()
# kekanan
senshi_y -= 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()


senshi_y -= 1
senshi_x -= 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()

    
senshi_y -= 1
senshi_x += 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()


senshi_y += 1
senshi_x -= 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()


senshi_y += 1
senshi_x += 1
if senshi_x < 0:
       print('Senshi makannya besok aja deh.')
       quit()
if senshi_y < 0:
    print('Senshi makannya besok aja deh.')
    quit()
if senshi_x != first_monster_x or senshi_y != first_monster_y:
    if senshi_x != second_monster_x or senshi_y != second_monster_y:
        if senshi_x != third_monster_x or senshi_y != third_monster_y:
            if senshi_x != fourth_monster_x or senshi_y != fourth_monster_y:
                if senshi_x != fifth_monster_x or senshi_y != fifth_monster_y:
                    if senshi_x != sixth_monster_x or senshi_y != sixth_monster_y:
                        if senshi_x != seventh_monster_x or senshi_y != seventh_monster_y:
                            if senshi_x != eighth_monster_x or senshi_y != eighth_monster_y:
                                if senshi_x != room_x or senshi_y != room_y:
                                    print('Senshi makan hari ini!')
                                    quit()
                                else:
                                    print('Senshi makannya besok aja deh.')
                                    quit()
                            else:
                                print('Senshi makannya besok aja deh.')
                                quit()    
                        else:
                            print('Senshi makannya besok aja deh.')
                            quit() 
                    else:
                        print('Senshi makannya besok aja deh.')
                        quit()
                else:
                    print('Senshi makannya besok aja deh.')
                    quit()               
            else:
                print('Senshi makannya besok aja deh.')
                quit()
        else:
            print('Senshi makannya besok aja deh.')
            quit()
    else:
        print('Senshi makannya besok aja deh.')
        quit()
else:
    print('Senshi makannya besok aja deh.')
    quit()
