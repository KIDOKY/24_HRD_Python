def even_odd(number: int) -> None:
    if number % 2 == 1:
        result = "홀수 입니다."
    else:
        result = "짝수 입니다."
    return result
print(even_odd(number = 5))

#======================================================
def besu5(n):
    if n % 5 == 0:
        rel = True
    else:
        rel = False

    return rel

num = int(input("양의 정수를 입력하세요: "))
result = besu5(num)

if result == True:
    print("%d -> 5의 배수이다." % num)
else:
    print("%d -> 5의 배수가 아니다." % num)
#======================================================
# 연습문제 7-2. 반환 값 이용한 3의 배수 합계
def sum_besu3(n):
    sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            sum = sum + i
    return sum

num = int(input("양의 정수를 입력하세요: "))
result = sum_besu3(num)

print("1 ~ %d까지의 정수 중 3의 배수의 합: %d" % (num, result))
#=======================================================
# 연습문제 7-3. 반환 값 이용한 원 면적과 원주
def cir_area(radius) :
    area = radius * radius * 3.14
    return area

def cir_circum(radius) :
    circum = 2 * 3.14 * radius
    return circum

def cir_height(radius, h):
    height = radius * radius * 3.14 * h
    return height

r = float(input('반지름을 입력하세요: '))
h = float(input("높이를 입력하세요: "))
a = cir_area(r)
b = cir_circum(r)
c = cir_height(r, h)
print('원의 면적 : %.2f, 원주의 길이 : %.2f, 원기둥의 부피 : %.2f' % (a, b, c))
#=======================================================
def computeMaxGong(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            result = i
    return result
#=======================================================
def calculate_volume(radius: float, height: float) -> float:
    return (radius ** 2 * 3.14 * height)

radius = float(input("반지름은? "))
height = float(input("높이는? "))
volume = calculate_volume(height=height,radius=radius)
print(f"엔진의 실린더의 부피 : {volume}")
#=======================================================
