phones: dict = {"갤럭시S5": 2014, "갤럭시S7": 2016, "갤럭시 노트8": 2017,
                "갤럭시 S9": 2018,}
for key in phones:
    print(phones[key])
print(len(phones))

#----------------------------------------------------------
scores = {"김채린":85, "박수정":98, "함수희":94, "안예린":90, "연수진":93}
sum = 0

for key in scores:
    sum = sum + scores[key]
    print("%s: %d" % (key, scores[key]))
avg = sum / len(scores)
print("합계: %d, 평균: %.2f" % (sum, avg))