maior = 0
local = 0
for i in range(100):
    num = int(input())
    if num >= maior:
        maior = num
        local = i+1
print(maior)
print(local)