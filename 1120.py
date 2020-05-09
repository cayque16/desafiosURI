while True:
  tecla,texto = input().split(" ")
  if tecla == '0' or texto == '0':
    break  
  texto = texto.replace(tecla,'')
  if texto != '':
    print(int(texto))
  else:
    print('0')