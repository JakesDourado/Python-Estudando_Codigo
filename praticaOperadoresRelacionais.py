nome = input('Digite o nome do aluno: ')
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2)/2

if(media >= 7 and media <=10):
	print ('Aluno',nome,'foi APROVADO com media',media)
elif(media >= 3 and media < 7):
	print ('Aluno',nome,'foi para RECUPERAÇÃO com media',media)
elif(media < 3 and media >=0):
	print ('Aluno',nome,'foi REPROVADO com media',media)
else:
	print ('Valor digitado é inválido!')

