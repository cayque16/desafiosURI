entrada1 = input().split(" ")
cod1 = int(entrada1[0])
num1 = int(entrada1[1])
valor1 = float(entrada1[2])
entrada2 = input().split(" ")
cod2 = int(entrada2[0])
num2 = int(entrada2[1])
valor2 = float(entrada2[2])

valor1 *= num1
valor2 *= num2

total = valor1 + valor2

print (str("VALOR A PAGAR: R$ ") + str("{:0.2f}".format(total)))
