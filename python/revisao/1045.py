a,b,c = map(float,input().split(" "))
lista = []
lista.append(a)
lista.append(b)
lista.append(c)

lista.sort(reverse=True)

a,b,c = lista[0],lista[1],lista[2]

if a >= b + c:
    print("NAO FORMA TRINAGULO")
    exit()
elif a ** 2 == b ** 2 + c ** 2:
    print("TRIANGULO RETANGULO")
elif a ** 2 > b ** 2 + c ** 2:
    print("TRIANGULO OBTUSANGULO") 
elif a ** 2 < b ** 2 + c ** 2:
    print("TRIANGULO ACUTANGULO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a) or (b == a and b != c) or (c == a and c != b) or (c == b and c != a):
    print("TRIANGULO ISOSCELES")
print("")