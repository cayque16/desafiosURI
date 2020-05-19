vetor = []
for i in range(100):
    vetor.append(float(input()))

for i,num in enumerate(vetor):
    if num <= 10:
        print("A[{}] = {:.1f}".format(i,num)) 
