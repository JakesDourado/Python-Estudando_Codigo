class ClassePai:
   a = 1 # atributo publico
   __b = 2 # atributo privado a class ClassePai

class ClasseFilha(ClassePai):
   __c = 3 # atributo privado a ClasseFilha
   
   def __init__(self):
     print (self.a)
     print (self.__c)

instancia_pai = ClassePai()
print (instancia_pai.a) # imprime 1

instancia_filha = ClasseFilha()
print (instancia_filha.__b )# Erro, pois __b é privado a classe ClassePai.
print (instancia_filha.__c) # Erro, __c é um atributo privado, somente chamado pela classe.
