salario = float(input())
imposto = 0

if salario >= 2000.01 and salario <= 3000:
  imposto = (salario-2000)*0.08
elif salario >= 3000.01 and salario <= 4500:
  imposto = 80 + (salario-3000)*0.18
elif salario > 4500:
  imposto = 80 + 270 + (salario-4500)*0.28
print("R$ {:.2f}".format(imposto)) if imposto > 0 else print("Isento")