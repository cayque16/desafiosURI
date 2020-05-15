dados = {
    '1': 0,
    '2': 0,
    '3': 0
}
while True:
    i = input()
    if i == '4':
        break
    try:
        dados[i] += 1
    except:
        continue
print("MUITO OBRIGADO")
print("Alcool: {}".format(dados['1']))
print("Gasolina: {}".format(dados['2']))
print("Diesel: {}".format(dados['3']))