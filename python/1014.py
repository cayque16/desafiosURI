distancia = int(input())
combustivel = float(input())

consumo  = distancia/combustivel

print(str("{:.3f}".format(consumo))+str(" km/l"))