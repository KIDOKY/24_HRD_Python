# 소비형 함수
# Consumer function
def function(param_name: int) -> None:
    result = param_name + 10
    print(result)
    print("나는 소비형")

result = function(param_name=10)
print(type(result))
#=======================================================
# 생산형 Supplier

def supply_function() -> tuple:
    (x, y) = (10, 20)
    print(sum)
    return (x, y)

(result1, result2) = supply_function()
print(result)
#=======================================================
# 함수형 functional

def functional_function(param: int) -> int:
    result = param + 1_000
    return result

result = functional_function(param = 100)
print(result)

#=======================================================
#Show, display function

def show_function():
    print("잔액 : 2000")
    print("계좌 : 2090-10-222")
    print("계좌입금 불가능")
    print("계좌출금 불가능")

show_function()
#=======================================================

def swapping_values(value1: int, value2: int) -> tuple:
    return (value2, value1)

def swapping_values2(value1, value2):
    return (value2, value1)

result2 = swapping_values(1_234, 4_321)
print(result2)

#=======================================================
def hello() : print("안녕하세요!")

hello()
hello()
hello()
#=======================================================