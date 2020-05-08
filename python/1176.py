casos = int(input())
while casos > 0:
  num = int(input())
  cont = num
  num1 = 0
  num2 = 1
  fib = 0
  while cont > 0:
      temp = fib
      fib = num1 + num2
      num1,num2 = temp,fib
      cont -= 1
  print("Fib({}) = {}".format(num,fib))
  casos -= 1