import re
casos = int(input())

for i in range(casos):
    palavra = input()
    if len(palavra) == 5:
        print(3)
    else:
        # print(re.search(r'.ne|o.e|on.', palavra))
        if re.search(r'.ne|o.e|on.', palavra) is not None:
            print(1)
        else:
            print(2)



# one
# *ne
# o*e
# on*
# two
# *wo
# t*o
# tw*