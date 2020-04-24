tempo = int(input())
velocidade = int(input())

distancia = tempo*velocidade
combustivel = distancia/12

print("{:.3f}".format(combustivel))