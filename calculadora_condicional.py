#coding: utf-8
print ('[1] - Somar \n[2] - Subtrair')
operacao = int(input('Digite uma opção: '))


num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))

if(operacao == 1):
	soma = num_1 + num_2
	print ('A soma deu [',soma,']')
else:
	sub = num_1 - num_2
	print ('A subtração deu [',sub,']')
