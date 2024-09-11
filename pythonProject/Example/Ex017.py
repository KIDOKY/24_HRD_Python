# Local 변수 (지역 변수) (auto) int value = 10; (static) int value = 20;
value_1:int = 10
value_2:int = 20

def swapping() -> None:
    temporary: int = 0
    global value_1
    global value_2
    print(f"바뀌기 전 : {value_1} : {value_2}")
    temporary = value_1
    value_1 = value_2
    value_2 = temporary
    print(f"바뀐 후 : {value_1} : {value_2}")

swapping()
print(f"원본값 - {value_1} : {value_2}")
#============================================================================
# 연습문제 7-4. 세 수중 가장 큰 수 찾기
def maxTwo(i,j):
    if i > j:
        return i
    else:
        return j
def maxThree(x,y,z):
    return maxTwo(maxTwo(x,y), maxTwo(y,z))

a = int(input('첫 번째 수를 입력하세요: '))
b = int(input('두 번째 수를 입력하세요: '))
c = int(input('세 번째 수를 입력하세요: '))
max_num = maxThree(a, b, c)
print('%d, %d, %d 중 가장 큰 수 : %d' % (a, b, c, max_num))
#============================================================================
# 연습문제 7-5. 최소 공배수 구하기
def computeMinGong(x, y):
    if x > y :
        big = x
    else :
        big = y
    while(True):
        if((big % x == 0) and (big % y == 0)):
            result = big
            break
        big = big + 1

    return result

num1 = int(input("첫 번째 수를 입력하세요: "))
num2 = int(input("두 번째 수를 입력하세요: "))
min_gong = computeMinGong(num1, num2)
print('%d와 %d의 최소공배수 : %d' % (num1, num2, min_gong))
#============================================================================