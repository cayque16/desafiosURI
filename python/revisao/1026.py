# CORRIGIR
# 	Time limit exceeded
def circuito(a,b):
  return (not a and b) or (a and not b)

def acrecenta_zero(texto,tam_final):
  tam_final -= len(texto)
  while tam_final > 0:
    texto = '0' + texto
    tam_final -= 1
  return texto

while True:
    try:
        a,b = map(int,input().split(" "))

        bin_de_a = bin(a)[2:]
        bin_de_b = bin(b)[2:]

        tam_a, tam_b = len(bin_de_a), len(bin_de_b)

        if tam_a > tam_b:
          bin_de_b = acrecenta_zero(bin_de_b,tam_a)
        elif tam_b > tam_a:
          bin_de_a = acrecenta_zero(bin_de_a,tam_b)

        result = ''
        for (i,j) in zip(bin_de_a,bin_de_b):
            if (circuito(int(i),int(j))):
                result += '1'
            else:
                result += '0'

        print(int(result, 2))
    except EOFError:
        break
