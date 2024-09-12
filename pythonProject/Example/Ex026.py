import math
print(math.sin(10))
print(math.floor(3.6))
print(math.ceil(5.1))
print(round(6.3))
print(math.factorial(100))
#==================================================================
# import random
# again = 'y'
# count = 1
# while again == 'y':
#     print('-' * 30)
#     print('주사위 던지기 : %d번째' % count)
#     me = random.randint(1, 6)
#     computer = random.randint(1, 6)
#     print('나 : %d' % me )
#     print('컴퓨터 : %d' % computer)
#
#     if me > computer:
#         print('나의 승리!')
#     elif me == computer:
#         print('무승부!')
#     else:
#         print('컴퓨터의 승리!')
#
#     count = count + 1
#     again = input('계속하려면 y를 입력하세요!')
# ==================================================================
from random import randint

my_win_count = 0
your_win_count = 0
iteration = 0
while iteration < 500:
    # print(randint(1,6))
    my_dice = randint(1,6)
    your_dice = randint(1,6)
    print(f"My dice : {my_dice}")
    print(f"Your dice : {your_dice}")
    if my_dice > your_dice:
        my_win_count += 1
        print("I won!")
    elif my_dice == your_dice:
        print("Draw")
    else:
        your_win_count += 1
        print("You won!")

    iteration += 1
    # input()
print("*" * my_win_count)
print("@" * your_win_count)
# ==================================================================