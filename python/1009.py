result = None
sal = None
vendas = None
nome = None

def read_string():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


nome = read_string()
sal = read_numeric()
vendas = read_numeric()
result = vendas * 0.15
result = result + sal
print(str("TOTAL = R$ ") + str("{:0.2f}".format(result)))