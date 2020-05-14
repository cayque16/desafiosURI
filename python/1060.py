nums = []
cont = 0
for i in range(6):
    nums.append(float(input()))
    if nums[i] > 0:
        cont += 1
print("{} valores positivos".format(cont))