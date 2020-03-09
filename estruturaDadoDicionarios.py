'''
#declarando um dicionario com alguns elementos (Chave:valor)
dic_pernambucano = {'Sport':41,'Santa Cruz':29,'Nautico':21}

#adicionando um elemento ao dicionario (Chave:valor)
dic_pernambucano['Salgueiro'] = 0
print dic_pernambucano

#buscando um valor com base na chave
quant_titulos = dic_pernambucano.get('Sport')
print 'O Sport tem',quant_titulos,'titulos'

#remover um elemento com base na chave
del dic_pernambucano['Salgueiro']
print dic_pernambucano

#remove a chave e retorna seu valor
valor = dic_pernambucano.pop('Nautico')
print 'O valor retornado da chave Nautico eh:',valor
print dic_pernambucano

#verificar se uma chave existe no dicionario
print 'Santa Cruz' in dic_pernambucano

#pegar todas as chaves do dicionario
print dic_pernambucano.keys()

#pegar todos os valores do dicionario
print dic_pernambucano.values()
'''

#declarando um dicionario com alguns elementos (Chave:valor)
dic_pernambucano = {'Sport':41,'Santa Cruz':29,'Nautico':21}

#Retornando elementos aleatorios
print (dic_pernambucano.popitem())

dic_paulista = {'Corinthians':29, 'Palmeiras':22, 'Santos':22}

#mesclar dois dicionarios
dic_pernambucano.update(dic_paulista)
print (dic_pernambucano)

#iterando em um dicionaios (simular a listas)
for elemento in dic_pernambucano:
	print (elemento) #retorna as chaves
	print (dic_pernambucano[elemento]) #retorna os valores

#iterando em um dicionaios (simular a listas)
for elemento in dic_pernambucano.values():
	print (elemento) #retorna apenas os valores

#converter um dicionario em uma lista
print (list(dic_pernambucano))