a,b,c = map(float,input().split(" "))

teste1 = abs(b-c) < a < b + c
teste2 = abs(a-c) < b < a + c
teste3 = abs(a-b) < c < a + b

if teste1 and teste2 and teste3:
    print("Perimetro = {:.1f}".format(a+b+c))
else:
    print("Area = {:.1f}".format(((a+b)*c)/2))