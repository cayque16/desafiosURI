while True:
  try:
    texto = input()
    texto = texto.replace('@','a').replace('&','e').replace('!','i').replace('*','o').replace('#','u')
    print(texto)
  except EOFError:
    break