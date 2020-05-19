vetor = []
for i in range(20):
    vetor.append(int(input()))

j = -1
for i in range(10):
    temp = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = temp
    j -= 1
for i,num in enumerate(vetor):
    print("N[{}] = {}".format(i,num))