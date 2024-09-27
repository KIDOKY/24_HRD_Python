colors: list = ['black', 'white', 'red', 'blue']
print(colors[0])    # get
colors[0] = ['yellow', 'cyan']    # set
print(colors[0])    # get(read)
print(colors)
for i in colors:
    print(i)

sliced_colors = colors[1:]
print(sliced_colors)
numbers = list(range(0, 1001))
print(numbers)

# [:] -> slice operator
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list(range(0, 10)) # 0 ~ 9
# new_numbers = [range(10)]
# print(new_numbers)

#-----------------------------------------------------------

v = [1, 2, 3]
V = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
value1 = V[0][0]    # get == read
print(value1)
values1 = V[0]  #scalar
print(values1)  # 리스트 타입

for i in range(0, 3):   # row
    for j in range(0, 3):   # column
        scalar = V[i][j]
        print(scalar, end ="\t")
    print()

    animals: list = ['사자', '토끼', '하이에나', '기린']
    index = 0
    size = len(animals)
    while index < size:
        animal: str = animals[index]
        print(animal, end = ", ")
        index += 1  # ++index, index++ 없다.

#------------------------------------------------------------
# 연습문제 5-1. 리스트로 만든 영어 스펠링 퀴즈
questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answers = ['a', 'u', 't','p']
for i in range(len(questions)) :
    q = '%s 에서 밑줄(_) 안에 들어갈 알파벳은?' % questions[i]
    ans = input(q)
    if ans == answers[i]:
        print('정답입니다!')
    else :
        print('틀렸습니다!')
#-------------------------------------------------------------
