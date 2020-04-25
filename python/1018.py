valor = int(input())

notas100 = int(valor/100)
resto = round(valor % 100,2)

notas50 = int(resto/50)
resto = round(resto % 50,2)

notas20 = int(resto/20)
resto = round(resto % 20,2)

notas10 = int(resto/10)
resto = round(resto % 10,2)

notas5 = int(resto/5)
resto = round(resto % 5,2)

notas2 = int(resto/2)
resto = round(resto % 2,2)

notas1 = int(resto)

print("{}".format(valor))
print(str(notas100)+str(" nota(s) de R$ 100,00"))
print(str(notas50)+str(" nota(s) de R$ 50,00"))
print(str(notas20)+str(" nota(s) de R$ 20,00"))
print(str(notas10)+str(" nota(s) de R$ 10,00"))
print(str(notas5)+str(" nota(s) de R$ 5,00"))
print(str(notas2)+str(" nota(s) de R$ 2,00"))
print(str(notas1)+str(" nota(s) de R$ 1,00"))