i=1
j=7
cont = 1
while i <= 9:
  print("I={} J={}".format(i,j))
  j -= 1
  if cont%3 == 0:
    i += 2
    j = 7
  cont += 1