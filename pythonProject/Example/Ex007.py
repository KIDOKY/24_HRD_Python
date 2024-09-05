i = 1
sum = 0
while i <= 100:
     sum += i
     print(f"{i} : {sum}")
     i += 1

print("총합은 : ", sum)
print("#" * 100)

# s = "Python is widely used by a number of big companies"
# i = 0
# count = 0
# while  i <= len(s) - 1:
#     if s[i] == 'a' or s[i] == 'A' or s[i] == 'e' or s[i] == 'E' or s[i] == 'i' or s[i] == 'I' or s[i] == 'o' or s[i] == 'O' or s[i] == 'u' or s[i] == 'U':
#         ++count
#
# print("모음 : ", end = " ")
# print(f"모음 갯수 : {count}")

index = len("Python") - 1
print("Python".upper())
s = "Python is widely used by a number of big companies"
word = s.lower()
print(word)
i = 0
count = 0
size = len(word)
while i < size:
    if word[i] == 'a' or word[i] == 'i' or word [i] == 'e' or \
            word[i] == 'u' or word[i] == 'o':
        print(f"모음 : {word[i]}")
        count += 1
    i += 1

print(f"모음의 갯수는 : {count}")