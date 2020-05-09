class Personagem():
  def __init__(self,vence,perde):
    self.vence = vence
    self.perde = perde

TESOURA = 'tesoura'
PAPEL = 'papel'
PEDRA = 'pedra'
LAGARTO = 'lagarto'
SPOCK = 'Spock'

personagens = {
    TESOURA: Personagem([PAPEL,LAGARTO],[SPOCK,PEDRA]),
    PAPEL: Personagem([PEDRA,SPOCK],[LAGARTO,TESOURA]),
    PEDRA: Personagem([LAGARTO,TESOURA],[PAPEL,SPOCK]),
    LAGARTO: Personagem([SPOCK,PAPEL],[PEDRA,TESOURA]),
    SPOCK: Personagem([PEDRA,TESOURA],[PAPEL,LAGARTO])
}

casos = int(input())
for i in range(1,casos+1):
  sheldon,raj = input().split(" ")
  if (sheldon in (personagens[raj].perde)):
    print('Caso #{}: Bazinga!'.format(i))
  elif (sheldon in (personagens[raj].vence)):
    print('Caso #{}: Raj trapaceou!'.format(i))
  else:
    print('Caso #{}: De novo!'.format(i))