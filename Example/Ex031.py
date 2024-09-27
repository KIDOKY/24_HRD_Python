# number = input("정수 입력 ")
# last_character = number[-1]
# if last_character in "02468":
#     print("짝수입니다.")
# if last_character in "13579":
#     print("홀수입니다.")

#======================================================

# number = int(input("정수 입력 :"))
# if number > 0:
#     # pass    # print()
#     raise NameError
# else:
#     print("음수이다.")

#======================================================

values = [1, 2, 3, 4, 5]
values.insert(0, 0)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers1 = [_ for _ in range(100)]
print(numbers1)
numbers2 = list(range(100))
print(numbers2)

numbers3 = list()
for i in range(100):
    numbers3.append(i)
print(numbers3)

#======================================================

list_values = [1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
error = 0
while error in list_values:
    list_values.remove(error)
print(list_values)

#======================================================

scores = [10, 20, 30, 40, 50]
summation = 0
for element in scores:
    summation += element
print("총합은 : {0}".format(summation))
print(f"총합은 : {sum(scores)}")

#======================================================

list_a = [1, 2, 3, 4, 5, 6, 7]
reversed_list_a = reversed(list_a)
print(f"list_a: {list_a}")
# print(reversed_list_a)
# for element in reversed_list_a:
#     print(element, end = "  ")
list_a.reverse()
print(f"list_a : {list_a}")

#======================================================

