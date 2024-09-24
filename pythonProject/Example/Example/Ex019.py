scores = ['안소영 97 80 93 97 93',
    '정예린 86 100 93 86 90',
    '김세린 91 88 99 79 92',
    '연수정 86 100 93 89 92',
    '박지아 80 100 95 89 90']

data = ""   # empty string 빈 문자열
for item in scores :
    data = data + item + '\n'

print(data)

# 파일(scores.txt)에 출력하기
file = open(file = 'scores.txt', encoding = 'UTF-8', mode = 'w')
file.write(data)
file.close()

# 파일 읽어 오기
file = open(file = 'scores.txt', encoding = 'UTF-8', mode = 'r')
lines = file.readlines()
print(lines)

for line in lines :
    print(line, end="")
file.close()

file = open(file = 'scores.txt', encoding = 'UTF-8', mode = 'r')
line_one = ""
