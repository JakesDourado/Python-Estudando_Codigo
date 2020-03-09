class Pessoa:
    def __init__(self, nome ='', idade=0):
       self.nome = nome
       self.idade = idade

    def calcular_lucro(self):
      return 'Podemos retornar o lucro!'

class PessoaFisica(Pessoa):

    def __init__(self, CPF, nome='', idade=0):
       super().__init__(nome, idade)
       self.CPF = CPF

    def __str__ (self):
      return '{} - {} - {}'.format(self.nome, self.idade, self.CPF)

    def calcula_taxa(self, salario, portentual):
      return ((salario*portentual)/100)


class PessoaJuridica(Pessoa):

    def __init__(self, CNPJ, nome='', idade=0):
       Pessoa.__init__(self, nome, idade)
       self.CNPJ = CNPJ

    def __str__ (self):
      return '{} - {} - {}'.format(self.nome, self.CNPJ, self.idade)
    
    def calcula_taxa(self, faturamento, portentual):
      return ((faturamento*portentual)/100) + 20

pessoa = PessoaFisica('122.333.332-1', 'Felipe', 28)
banco = PessoaJuridica('00.000.000/0001-11', 'Banco do Brasil', 435)
print (pessoa)
print (banco)

print (pessoa.calcular_lucro())
print (pessoa.calcula_taxa(1525, 5))

print (banco.calcular_lucro())
print (banco.calcula_taxa(1000000, 5))


