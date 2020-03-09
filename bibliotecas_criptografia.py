#chamar uma funcao do seu modulo separadamente
from criptografia import cripografar

#chamar todo o modulo e apelidar de forma menor
import criptografia as cp



while True:
	global mensagem

	opcao = int(input('Menu: \n [1] - Cripografar \n [2] - Descripografar \n [3] - Sair \n'))
	if (opcao == 1):

		#criando uma mensagem
		mensagem = input('Digite uma mensagem: \n')

		#chamando o metodo cripografar do nosso modulo
		mensagem_criptografada = cp.cripografar(mensagem)
		#mostrando o resultado da nossa cripografia
		print ('Mensagem criptografada com sucesso!\n',mensagem_criptografada)
	elif (opcao == 2):
		#mostrando que agora vamos decriptografar
		#print ('Agora vamos decriptografar a mensagem [',mensagem,']')

		#chamando nosso metodo descripografar do nosso modulo
		mensagem_descriptografada = cp.descripografar(mensagem_criptografada)

		#mostrando o resultado da mensagem descripografada
		print ('Mensagem descripografada com sucesso!\n',mensagem_descriptografada)
	elif(opcao ==3):
		break
	else:
		print('Digite uma opcao valida!')







