import pdb

#coding: utf-8
num = int(input('Digite um numero: '))	

pdb.set_trace()
if(num == 1): #primeiro nivel
	print ('Mensagem para condição 1', num)
elif(num == 2):
	print ('Mensagem para condição 2', num)
elif(num == 3):
	print ('Mensagem para condição 3', num)
else:
	print('Você não digitou nenhum número esperado!')
