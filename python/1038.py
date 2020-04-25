cod,quant = map(int,input().split(" "))

produtos =  [4,4.5,5,2,1.5]

cod -= 1

print("Total: R$ {:.2f}".format((produtos[cod]*quant)))