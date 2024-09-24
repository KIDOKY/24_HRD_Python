scores = [[75, 83, 90], [86, 86, 73], [76, 95, 83],
          [89, 96, 69], [89, 76, 93], [10, 20, 30]]

for i in range(len(scores)):
    for j in range(len(scores[i])):
        score = scores[i][j]
        print(score, end= "\t")
    print()
print("-" * 30)
#--------------------------------------------------
strings = [['잠자리', '풍뎅이', '여치'], ['짜장면', '파스타', '피자', '국수']]
for i in range(len(strings)) :
    for j in range(len(strings[i])) :
        print(strings[i][j])
    print()
    print("-" * 30)
#---------------------------------------------------
(x, y, z) = (10, 20, 30)    # tuple
X1: tuple = (10,20,30)      # tuple
X2: list = [10, 20, 30]     # list
print("-" * 30)
#---------------------------------------------------
menutuple = ('짜장면', '우동', '짬뽕', '볶음밥')
print(menutuple)
print(menutuple[0])
print(menutuple[2])
print(menutuple[0:3])
#menutuple[1] = '사천탕면'
print("-" * 30)
#---------------------------------------------------
tup1 = (10,20,30)
tup2 = (40,50,60)
tup3 = tup1 + tup2
print(tup3)
print(len(tup3))
print("-" * 30)
#---------------------------------------------------
element1 = (1,)
print(type(element1))
print("-" * 30)
#---------------------------------------------------
dans = (2, 3, 4, 5, 6, 7, 8, 9)

print("구구단표")
print("=" * 50)

for dan in dans:
    print(str(dan) + "단")

    for i in range(1,10):
        print("%d x %d = %d" % (dan, i, dan * i))
    print("-" * 30)
#---------------------------------------------------
admin = ('rubato', '12345', 'rubato@naver.com')
print('- 관리자 정보')
print('아이디 : ' + admin[0])
print('비밀번호 : ' + admin[1])
print('이메일 : ' + admin[2])
print("-" * 30)
#---------------------------------------------------
name = '홍지수'
scores = {'kor': 90, 'eng': 89, 'math': 95, 'science': 88}
print(scores)
scores['kor'] = 70
print(scores['kor'])
scores['music'] = 100
print(scores)
del scores['science']
print(scores)
print('이름 : %s' % name)
print('국어 : %s' % scores['kor'])
print('영어 : %s' % scores['eng'])
print('수학 : %s' % scores['math'])
print("-" * 30)
#---------------------------------------------------
phones = {'갤럭시 S5': 2014, '갤럭시 S7': 2016, '갤럭시 노트8': 2017, '갤럭시 S9': 2018}
print(phones)
for key in phones :
    print('%s => %s' % (key, phones[key]))
print(len(phones))
print("-" * 30)
#---------------------------------------------------