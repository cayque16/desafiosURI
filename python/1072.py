casos = int(input())
sim,nao = 0,0

for i in range(casos):
    num = int(input())
    if num in range(10,21):
        sim += 1
    else:
        nao += 1
print("{} in".format(sim))
print("{} out".format(nao))