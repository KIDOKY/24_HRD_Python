# 빈 리스트에 요소 추가
scores:list = list() # [] empty list

while True:
    score: int = int(input("점수를 입력하세요: "))

    if score == -1:
        break
    else:
        scores.append(score)

print("총 과목들은 : ", scores)

summation = 0
for subject in scores:
    summation += subject

print(f"총 점수는 : {summation}")
print(f"평균은 : {summation / len(scores)}")
#-------------------------------------------------
# 두 리스트를 하나로 합치기
person1 = ["kim", 24, "kim@naver.com"]
person2 = ["lee", 35, "lee@hanmail.net"]

person = person1 + person2
print(person)
#-------------------------------------------------
numbers = [[10, 20, 30], [40, 50, 60, 70, 80]]

print(numbers[0][0])
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])
#--------------------------------------------------
numbers = [[10, 20, 30], [40, 50, 60, 70, 80]]
for i in range(len(numbers)) :
    for j in range(len(numbers[i])) :
        print('numbers[%d][%d] = %d' % (i, j, numbers[i][ j]))
#--------------------------------------------------
