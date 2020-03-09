
'''
num = 0
while (num < 20):
	print ('Estamos na iteração',num)
	num += 1	
	#num = num + 1

print ('Parou pois o numero chegou a',num)


cond = True
num = 0

while (cond == True):
	print('Estamos na iteração',num)
	num += 1

	if(num == 20):
		cond = False
else:
	print ('Status da condição agora está False')



cond = True

while (cond == True):
	print('Entramos no laço pois a condição é',cond)
	cond = False
	
	print('Mudamos o estado da condição para',cond)
	print('Agora paramos o programa com o break')
	
	break
else:
	print ('Não chegamos aqui!')

'''


'''
A instrução continue é usada para pular o restante do 
código dentro de um loop apenas para a iteração atual. 
Loop não termina mas continua com a próxima iteração
'''

num = 0

while (num < 20):
	num+=1
	if (num == 5):
		print ('Entramos no bloco e vamos continuar')
		continue
else:
	print ('Chegamos aqui!')
