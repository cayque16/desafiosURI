dias = int(input())

anos = int(dias/365)
dias -= anos*365
meses = int(dias/30)
dias -= meses*30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))