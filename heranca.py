#declarando uma classe modelo
class Carro():
	def __init__ (self, marca = None, ano = None):
		self.marca = marca
		self.ano = ano
#criando uma classe Gol que herda de Carro
class Gol(Carro):
	def __init__ (self, marca, ano, airbag):
		#carrega no seu construtor o construtor da classe pai
		super().__init__(marca, ano)
		#cria seu atributo proprio da classe
		self.__airbag = airbag

	def __str__ (self):
		return '%s - %d - %s'%(self.marca, self.ano, self.__airbag)
#criando uma classe Fusca que herda de Carro
class Fusca(Carro):
	def __init__ (self, marca, ano, consumo, revenda):
		super().__init__(marca, ano)
		self.__consumo = consumo
		self.__revenda = revenda

	def __str__ (self):
		return '%s - %d - %d - %s'%(self.marca, self.ano, self.__consumo, self.__revenda)
fusquinha = Fusca('VW', 1870, 15, 'Bom')
golzeira = Gol('VW', 2015, True)
print (fusquinha)
print (golzeira)
