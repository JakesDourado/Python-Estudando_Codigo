'''
#Declarando uma classe basica
class MinhaPrimeiraClasse():


	#Declarando uma funcao para classe
	def funcao_da_classe(self, args):
		
		#retorno da funcao
		return args

	#Declarando uma funcao para classe
	def outra_funcao_da_classe(self):
		
		pass


self uma convencao para deixar explicito a instancia 
do objeto dentro da classe.
'''
'''
#declarando uma classe
class Pessoa():

	#criando o construtor para classe Pessoa
	def __init__(self):

		#atributos direto no construtor
		self.nome = 'Felipe'
		self.idade = 28

	def imprimir(self):
		print ('Me chamo %s e tenho %d anos'%(self.nome, self.idade))


#criando uma instancia de Pessoa
pessoa = Pessoa()

#chamando o metodo da classe
pessoa.imprimir()
'''
'''
#declarando uma classe
class Pessoa():

	#criando o construtor para classe Pessoa
	def __init__(self, nome, idade):

		#atributos direto no construtor
		self.nome = nome
		self.idade = idade

	def imprimir(self):
		print ('Me chamo %s e tenho %d anos'%(self.nome, self.idade))


#criando uma instancia de Pessoa
pessoa = Pessoa('Felipe', 28)

#chamando o metodo da classe
pessoa.imprimir()
'''
'''
#declarando uma classe
class Pessoa():

	#criando o construtor para classe Pessoa
	def __init__(self, nome, idade):

		#atributos privados
		self.__nome = nome
		self.__idade = idade

	#declarando nossos metodos de acesso dos atributos da classe
	def getNome(self):
		return self.__nome

	def getIdade(self):
		return self.__idade

	#declarando nosso metodos modificadores dos atributos da classe
	def setNome(self, nome):
		self.__nome = nome

	def setIdade(self, idade):
		self.__idade = idade


	def imprimir(self):
		print ('Me chamo %s e tenho %d anos'%(self.getNome(), self.getIdade()))


#criando uma instancia de Pessoa
pessoa = Pessoa('Felipe', 28)
#chamando o metodo da classe
pessoa.imprimir()

#mudando valor do nome usando o metodo modificador
pessoa.setNome('Paulo')

#chamando o metodo da classe
pessoa.imprimir()
'''

'''
#declarando uma classe
class Pessoa():

	#criando o construtor para classe Pessoa
	def __init__(self, nome, idade):

		#atributos privados
		self.__nome = nome
		self.__idade = idade

	#declaracao do metodo str
	def __str__ (self):
		return 'Nome [%s] - Idade [%d]'%(self.__nome, self.__idade)

	#declarando nossos metodos de acesso dos atributos da classe
	def getNome(self):
		return self.__nome

	def getIdade(self):
		return self.__idade

	#declarando nossos metodos modificadores dos atributos da classe
	def setNome(self, nome):
		self.__nome = nome

	def setIdade(self, idade):
		self.__idade = idade


#criando uma instancia de Pessoa
pessoa = Pessoa('Felipe', 28)
print (pessoa)
'''


#declarando uma classe
class Pessoa():
	#declarando os atribudos sem valores iniciais
	cpf = None

	def __init__ (self, nome, idade):
		self.__nome = nome
		self.__idade = idade

	#declaracao do metodo str
	def __str__ (self):
		return 'Nome [{}] - Idade [{}] - CPF [{}]'.format(self.__nome, self.__idade, self.cpf)

	#declarando nossos metodos de acesso dos atributos da classe
	def getNome(self):
		return self.__nome

	def getIdade(self):
		return self.__idade

	#declarando nossos metodos modificadores dos atributos da classe
	def setNome(self, nome):
		self.__nome = nome

	def setIdade(self, idade):
		self.__idade = idade

	def getCpf(self):
		return self.cpf
	
	def setCpf(self, cpf):
		self.cpf = cpf


#criando uma instancia de Pessoa
pessoa = Pessoa('Felipe', 28)
print (pessoa)
pessoa.setCpf(123)
print(pessoa)


'''
import datetime
#declarando uma classe
class Pessoa():
	#declarando os atribudos sem valores iniciais
	def __init__(self, nome, idade):
		self.__nome = nome
		self.__idade = idade

	#declaracao do metodo str
	def __str__ (self):
		return 'Nome [%s] - Idade [%d]'%(self.__nome, self.__idade)

	#declarando nossos metodos de acesso dos atributos da classe
	def getNome(self):
		return self.__nome

	def getIdade(self):
		return self.__idade

	#declarando nossos metodos modificadores dos atributos da classe
	def setNome(self, nome):
		self.__nome = nome

	def setIdade(self, idade):
		self.__idade = idade


	def calcular_nascimento(self, idade):
		return int(datetime.date.today().strftime("%Y")) - idade


#criando uma instancia de Pessoa
pessoa = Pessoa('Felipe', 28)
print (pessoa.calcular_nascimento(56))
'''

