casos = int(input())
maior = 0
palavras = []

def imprime_com_espacos(palavra, tam_final):
    while len(palavra) < tam_final:
        palavra = ' '+palavra
    print(palavra)


for i in range(casos):
    palavra = input()
    if len(palavra) > maior:
        maior = len(palavra)
    palavras.append(palavra)

for i in palavras:
    imprime_com_espacos(i, maior)