frase = input().split(" ")
frase_final = ""
cont = 0

for palavra in frase:
    if len(palavra) > 2:
        frase_final += palavra[0] + ". "
        cont += 1
    else:
        frase_final += palavra + " "

print(frase_final)
print(cont)