# 파일 읽어 오기
file = open(file = 'scores.txt', encoding = 'UTF-8', mode = 'r')
line_one = file.readline()
# print(lines)
#
# for line in lines :
#     print(line, end="")
print(line_one)

print(line_one.split(sep = ","))
line_one_values = line_one.split(sep = ",")
total = (
         int(line_one_values[1]) +
         int(line_one_values[2]) +
         int(line_one_values[3]) +
         int(line_one_values[4]) +
         int(line_one_values[5])
        )
print(f"TOTAL score : {total}")
file.close()