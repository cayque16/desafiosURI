vetor = []
for i in range(10):
    num = int(input())
    if num <= 0:
        vetor.append(1)
    else:
        vetor.append(num)
j = 0
for i in vetor:
    print("X[{}] = {}".format(j,i))
    j+= 1