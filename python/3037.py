casos = int(input())
for i in range(casos):
  joao,maria = 0,0
  for j in range(6):
    x,d = map(int,input().split(" "))
    if j < 3:
      joao += x*d
    else:
      maria += x*d
  if joao > maria:
    print("JOAO")    
  else:
    print("MARIA")