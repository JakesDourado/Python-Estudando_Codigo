#os.system('cls' if os.name == 'nt' else 'clear')
import os

cond = True
cont = 0
while (cond):

	print ('Menu:\n'+
			'[1] - Operacoes Aritimeticas\n'+
			'[2] - Manipulando Strings\n'+
			'[3] - Sair')

	opcao = int(input('Digite uma opcao: '))
	if(opcao == 1):
		
		os.system('cls' if os.name == 'nt' else 'clear')
		print ('Menu Operacoes Aritimeticas')
		num_1 = int(input('Digite o primeiro numero: '))
		num_2 = int(input('Digite o segundo numero: '))
		
		soma = num_1 + num_2
		sub = num_1 - num_2
		mult = num_1 * num_2


		print ('A soma dos numeros [',num_1,'] + [',num_2,'] eh [',soma,']')
		print ('A subtracao dos numeros [',num_1,'] - [',num_2,'] eh [',sub,']')
		print ('A multiplicacao dos numeros [',num_1,'] * [',num_2,'] eh [',mult,']')

	elif(opcao == 2):
		os.system('cls' if os.name == 'nt' else 'clear')
		
		print ('Menu Manipulando String:\n'+
		'[1] - Colocar tudo para MAIUSCULO\n'+
		'[2] - Separar uma String\n'+
		'[3] - Sair')

		#escopo interno
		opcao = int(input('Digite uma opcao: '))

		if (opcao == 1):
			os.system('cls' if os.name == 'nt' else 'clear')

			frase = input('Digite uma String: ')
			nova_frase = frase.upper()
			print ('A String [',frase,'] agora eh [',nova_frase,']')

		elif(opcao == 2):
			os.system('cls' if os.name == 'nt' else 'clear')

			frase = input('Digite uma String: ')
			print ('Sua frase eh [', frase,']\n')

			corte = input('Digite onde deseja cortar a String\n')
			nova_frase = frase.split(str(corte))

			print ('Sua NOVA frase eh [', nova_frase,']\n')

			
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			print ('Digite uma opcao valida!')


	elif (opcao == 3):
		os.system('cls' if os.name == 'nt' else 'clear')
		print ('Obrigado Volte Sempre!')
		cond = False
	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print ('Selecione uma opcao valida!')