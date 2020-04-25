a,b,c,d = map(int,input().split(" "))

teste1 = b > c
teste2 = d > a
teste3 = (c+d) > (a+b)
teste4 = (c%2==0) and (d%2==0)
teste5 = a%2==0

if(teste1 and teste2 and teste3 and teste4 and teste5):
	print("Valores aceitos")
else:
	print("Valores nao aceitos")