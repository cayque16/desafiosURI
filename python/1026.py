# CORRIGIR
# 	Time limit exceeded
def circuito(a,b):
  return (not a and b) or (a and not b)

def dec_to_bin(num):
  result = ''
  while num > 1:
    result += str(num % 2)
    num = num // 2
  result += str(num)
  if len(result) < 32:
    for i in range(32-len(result)):
      result += '0'
  return result

def bin_to_dec(num):
  mult = 1
  result = 0
  for i in num:
    result += int(i) * mult
    mult *= 2
  return result

while True:
    try:
        a,b = map(int,input().split(" "))

        bin_de_a = dec_to_bin(a)
        bin_de_b = dec_to_bin(b)

        result = ''
        for (i,j) in zip(bin_de_a,bin_de_b):
            if (circuito(int(i),int(j))):
                result += '1'
            else:
                result += '0'

        print(bin_to_dec(result))
    except EOFError:
        break