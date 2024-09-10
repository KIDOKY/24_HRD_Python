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