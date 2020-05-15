inter,gremio,empate,total = 0,0,0,0
while True:
    i,g = map(int,input().split(" "))
    if i > g:
        inter += 1
    elif g > i:
        gremio += 1
    else:
        empate += 1
    total += 1
    if input("Novo grenal (1-sim 2-nao)\n") == '2':
        break
print("{} grenais".format(total))
print("Inter:{}".format(inter))
print("Gremio:{}".format(gremio))
print("Empates:{}".format(empate))
if inter > gremio and inter > empate:
    print("Inter venceu mais")
elif gremio > inter and gremio > empate:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")