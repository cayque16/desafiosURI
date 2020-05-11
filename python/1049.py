CARNIVORO = 'carnivoro'
ONIVORO = 'onivoro'
HERBIVORO = 'herbivoro'
HEMATOFAO = 'hematofago'

entrada1 = input()
entrada2 = input()
entrada3 = input()

if entrada1 == "vertebrado":
    if entrada2 == "ave":
        if entrada3 == CARNIVORO:
            print("aguia")
        elif entrada3 == ONIVORO:
            print("pomba")
    elif entrada2 == "mamifero":
        if entrada3 == ONIVORO:
            print("homem")
        elif entrada3 == HERBIVORO:
            print("vaca")
elif entrada1 == "invertebrado":
    if entrada2 == "inseto":
        if entrada3 == HEMATOFAO:
            print("pulga")
        elif entrada3 == HERBIVORO:
            print("lagarta")
    elif entrada2 == "anelideo":
        if entrada3 == HEMATOFAO:
            print("sanguessuga")
        elif entrada3 == ONIVORO:
            print("minhoca")