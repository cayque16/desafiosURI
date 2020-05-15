valores = {
    'total': 0,
    'C': 0,
    'R': 0,
    'S': 0
}
casos = int(input())
for i in range(casos):
  quant,indice = input().split(" ")
  valores[indice] += int(quant)
  valores['total'] += int(quant)

print("Total: {} cobaias".format(valores['total']))
print("Total de coelhos: {}".format(valores['C']))
print("Total de ratos: {}".format(valores['R']))
print("Total de sapos: {}".format(valores['S']))
print("Percentual de coelhos: {:.2f} %".format(valores['C']/valores['total']*100))
print("Percentual de ratos: {:.2f} %".format(valores['R']/valores['total']*100))
print("Percentual de sapos: {:.2f} %".format(valores['S']/valores['total']*100))