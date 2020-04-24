# AINDA EM DESENVOLVIMENTO A SOLUÇÃO APRESENTA ERROS

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


valor = read_numeric()

notas100 = int(valor/100)
resto = valor % 100

notas50 = int(resto/50)
resto = resto % 50

notas20 = int(resto/20)
resto = resto % 20

notas10 = int(resto/10)
resto = resto % 10

notas5 = int(resto/5)
resto = resto % 5

notas2 = int(resto/2)
resto = resto % 2

moedas1 = int(resto/1)
resto = resto % 1

moedas050 = int(resto/0.5)
resto = resto % 0.5

moedas025 = int(resto/0.25)
resto = resto % 0.25

moedas010 = int(resto/0.10)
resto = resto % 0.10

moedas005 = int(resto/0.05)
resto = resto % 0.05

moedas001 = int(resto/0.01)
resto = resto % 0.01

print(str("NOTAS:"))
print(str(notas100)+str(" nota(s) de R$ 100.00"))
print(str(notas50)+str(" nota(s) de R$ 50.00"))
print(str(notas20)+str(" nota(s) de R$ 20.00"))
print(str(notas10)+str(" nota(s) de R$ 10.00"))
print(str(notas5)+str(" nota(s) de R$ 5.00"))
print(str(notas2)+str(" nota(s) de R$ 2.00"))
print(str("MOEDAS:"))
print(str(moedas1)+str(" moeda(s) de R$ 1.00"))
print(str(moedas050)+str(" moeda(s) de R$ 0.50"))
print(str(moedas025)+str(" moeda(s) de R$ 0.25"))
print(str(moedas010)+str(" moeda(s) de R$ 0.10"))
print(str(moedas005)+str(" moeda(s) de R$ 0.05"))
print(str(moedas001)+str(" moeda(s) de R$ 0.01"))