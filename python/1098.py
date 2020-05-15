i = 0
n = 0
while True:
    if i in [1,2,3,4,5]:
        i = int(i)

    print("I={} J={}".format(i,i+1))
    print("I={} J={}".format(i,i+2))
    print("I={} J={}".format(i,i+3))
    
    if i == 2:
        break
    else:
        i = round(i + 0.2,1)