segundos = int(input())

horas = int(segundos/3600)
segundos -= horas*3600
minutos = int(segundos/60)
segundos -= minutos*60

print("{}:".format(horas)+"{}:".format(minutos)+"{}".format(segundos))