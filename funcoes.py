
#declarando um metodo (sim, metodo pois nao retorna valor)
def meu_metodo():
	#dentro do escopo do metodo criamos nossas intrucoes
	print ('Nosso primeiro METODO em Python!')

#chamando um metodo
meu_metodo()

#declarando uma funcao
def minha_funcao():
	#dentro do escopo da funcao criamos nossas intrucoes

	#agora nos temos um retorno
	return 'Nossa primeira FUNCAO em Python!'

#chamando uma funcao,
#minha_funcao()
print (minha_funcao(), type(minha_funcao()))

#declarando uma funcao
def minha_funcao(num_1,num_2):
	#dentro do escopo da funcao criamos nossas intrucoes

	#agora nos temos um retorno
	return num_1+num_2

#chamando uma funcao
print (minha_funcao(5,5),type(minha_funcao(5,5)))



#parametros default
def minha_funcao(num_1=5, num_2=6):
	#dentro do escopo da funcao criamos nossas intrucoes

	#agora nos temos um retorno
	return num_1+num_2

#chamando uma funcao
print (minha_funcao())

#chamando uma funcao (alterando os parametros defaults)
print (minha_funcao(1,2))

#declarando uma funcao com alguns parametros	
def minha_funcao(num_1, num_2, num_3):

	#retorno da funcao
    return (num_1 + num_2) * num_3

#chamando a funcao passando valores de forma posicional
#vamos armazenar nosso retorno em uma variavel
resultado = minha_funcao(1,2,3)
#exibindo o resultado na tela
print (resultado)

#chamando a funcao passando valores de forma nomeada
resultado = minha_funcao(num_1 = 1, num_3 = 3, num_2 = 2)
#exibindo o resultado na tela
print (resultado)