import string
alfabeto = list(string.ascii_uppercase)
casos = int(input())
for i in range(casos):
  texto = input()
  cifra = int(input())
  texto = list(texto)
  result = ''
  for i in texto:
    pos = alfabeto.index(i)-cifra
    result += alfabeto[pos]

  print(result)