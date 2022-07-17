casos = int(input())

for i in range(casos):
    nome, forca = input().split(" ")
    print("Y") if nome == "Thor" else print("N")