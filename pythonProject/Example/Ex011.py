scores = [[1, 2, 3],[4, 5, 6, 7, 8],[9, 10, 11],[1]]
print(len(scores))

for i in range(len(scores)):
    for j in range(len(scores[i])):
        print(scores[i][j], end = "\t")
    print()
    #--------------------------------------------------
