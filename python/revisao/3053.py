def movimenta_moeda(pos_atual, movimentos):
	for mov in movimentos:
		if mov == 1:
			pos_atual = 'B' if pos_atual == 'A' else 'A'
		elif mov == 2:
			pos_atual = 'C' if pos_atual == 'B' else 'B'
		elif mov == 3:
			pos_atual = 'C' if pos_atual == 'A' else 'A'
	return pos_atual

print(movimenta_moeda('C', [1,2,3,3,1,1]))