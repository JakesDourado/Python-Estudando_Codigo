#Declarando uma classe chamada Vetor
class Vetor():

	#inicializando nosso construtor
	def __init__(self, vetor):
		self.__vetor = vetor

	#definindo nossa operacao de sobrecarga do operador de multiplicacao *
	def __mul__ (self, escalar):
		aux = []

		for element in vetor:
			aux.append(element * escalar)
		return aux

vetor = [3,2]
escalar = 2
#operacao sem a sobrecarga do operador de multiplicacao
u = vetor * escalar
print (u)
#criando uma instancia de Vetor e passando um vetor para o construtor
v = Vetor(vetor)
#operacao com sobrecarga do operador de multiplicacao
u = v * escalar
print (u)

