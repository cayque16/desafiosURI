entrada = input()

a = int(entrada.split(" ")[0])
n = int(entrada.split(" ")[-1])

soma = 0
for i in range(n):
    soma += a+i
print(soma)