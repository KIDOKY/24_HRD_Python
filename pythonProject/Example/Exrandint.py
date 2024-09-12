from random import randint

one_count = 0
two_count = 0
three_count = 0
four_count = 0
five_count = 0
six_count = 0
iteration = 0
# number = 0
while iteration < 100_000:
    number = randint(a = 1, b = 6)
    if number == 1:
        one_count += 1
    elif number == 2:
        two_count += 2
    elif number == 3:
        three_count += 1
    elif number == 4:
        four_count += 1
    elif number == 5:
        five_count += 1
    else :
        six_count += 1
    iteration += 1

print(f"One count : {one_count}")
print(f"Two count : {two_count}")
print(f"Three count : {three_count}")
print(f"Four count : {four_count}")
print(f"Five count : {five_count}")
print(f"Six count : {six_count}")

print("\r\n")

print("*" * (one_count // 50))
print("*" * (two_count // 50))
print("*" * (three_count // 50))
print("*" * (four_count // 50))
print("*" * (five_count // 50))
print("*" * (six_count // 50))