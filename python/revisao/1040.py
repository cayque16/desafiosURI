n1,n2,n3,n4 = map(float,input().split(" "))

media = (n1*2+n2*3+n3*4+n4)/10

print("Media: {:.1f}".format(media))
if(media >= 7):
	print("Aluno aprovado.")
elif(media < 5):
	print("Aluno reprovado.")
elif(media >= 5 and media <= 6.9):
	print("Aluno em exame.")
	exame = float(input("Nota do exame: "))
	
	mediaFinal = (media + exame)/2
	
	if(mediaFinal >= 5):
		print("Aluno aprovado.")
		print("Media final: {:.1f}".format(mediaFinal))
	elif(mediaFinal < 5):
		print("Aluno reprovado.")
		print("Media final: {:.1f}".format(mediaFinal))