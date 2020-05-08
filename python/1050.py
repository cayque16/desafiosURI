ddd = input()

dados = {
    '61': 'Brasilia',
    '11': 'Sao Paulo',
    '71': 'Salvador',
    '21': 'Rio de Janeiro',
    '32': 'Juiz de Fora',
    '19': 'Campinas',
    '27': 'Vitoria',
    '31': 'Belo Horizonte'
}
try:
  print(dados[ddd])
except:
  print("DDD nao cadastrado")