'''

palavra = 'tranquilo'

for indice, letra in enumerate(palavra):
	print (indice, letra)
'''


'''
A função enumerate() retorna o índice 
e o elemento associado em uma lista ao mesmo tempo.
'''

palavra = 'tranquilo'

for indice, letra in enumerate(palavra):
	if((letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u')):
		print ('No indice',indice,'tem a vogal',letra,'na palavra',palavra)