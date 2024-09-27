minimum = 0
maximum = 0

def find_gcm(input_value1:int, input_value2:int) -> int:
    if input_value1 > input_value2:
        maximum = input_value1
    else:
        minimum = input_value2
    gcm = 0
    for number in range(2, minimum + 1):
        if input_value1 % number == 0 and input_value2 % number == 0:
            gcm = number
    return gcm

input_value1 = int(input("첫 번째 입력: "))
input_value2 = int(input("두 번째 입력: "))

gcm = find_gcm(input_value2=input_value2, input_value1=input_value1)
print(f"최대공약수는 : {gcm}")
#==============================================================================
def is_prime_number(prime_number: int) -> bool:
    for number in range(2, prime_number + 1):
        if prime_number % number == 0:
            return False
    return True

prime_number = int(input("숫자를 입력해주세요. "))

result = is_prime_number(prime_number=prime_number)
if result:
    print("입력하신 숫자는 소수입니다.")
else:
    print("입력하신 숫자는 소수가 아닙니다.")
#==============================================================================
def matchWord(in_word, answer) :
    if in_word == answer :
        msg = '참 잘했어요~~~'
    else :
        msg = '단어 공부 좀 더 해야겠어요.ㅋㅋ'
    return msg

eng_dict = {'apple':'사과', 'lion':'사자', 'book':'책', 'love':'사랑', 'friend':'친구'}

for i in eng_dict:
    string = input(eng_dict[i] + '에 맞는 영어 단어는? ')
    result = matchWord(string, i)
    print(result)