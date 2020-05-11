nums = [6,2,5,5,4,5,6,3,7,6]
casos = int(input())
for n in range(casos):    
    entrada = input()
    total = 0
    for i in entrada:
        total += nums[int(i)]
    print("{} leds".format(total))