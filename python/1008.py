num = int(input())
horas = int(input())
sal = float(input())

print "NUMBER = ",num
print "SALARY = U$ ",horas*sal

# ALTERNATIVA
"""
result = None
num = None
sal = None
horas = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


num = read_integer()
horas = read_integer()
sal = read_numeric()
result = horas * sal
print(str("NUMBER = ") + str(num))
print(str("SALARY = U$ ") + str("{:0.2f}".format(result)))
"""
