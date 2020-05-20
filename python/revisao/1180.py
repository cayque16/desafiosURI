tam = int(input())
nums = list(map(int,input().split(" ")))
menor,pos = nums[0],0
for i,num in enumerate(nums):
  if num < menor:
    pos = i
    menor = num
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(pos))