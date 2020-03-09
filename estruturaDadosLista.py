
#Declarando uma lista vazia em Python
lista = []

#Declaracao explicita de lista
lista_2 = list((1,2,3)) 

#Declarando uma lista com alguns elementos
#Declaracao implicita de lista
lista_2 = ['C',4.65,True,'Vamos Aprender',['Outra','lista','interna']]

#Acessando um elemento de umas lista
print (lista_2[3])

#Fatiando uma lista
print (lista_2[2:5])

#Fatiando uma lista
print (lista_2[:3])

#Fatiando uma lista
print (lista_2[1:])

#Fatiando uma lista
print (lista_2[::2])


#Declarando uma lista vazia
lista = []

#Adicionando elementos em uma lista
lista.append('Python')
lista.append('Java')
lista.append('Php')
lista.append('C#')

print (lista)

#Inserir uma elemento em uma posicao especifica
lista.insert(3,'C++')
print (lista)

#Remover um elemento pelo seu valor
lista.remove('Java')
print (lista)

#Pegar o indice de um elemento pelo valor
indice = lista.index('Python')
print (indice)

#Removendo um elemento pelo indice
del(lista[3])
print (lista)

#Declarando uma lista com alguns elementos
lista = ['Primeiro','Segundo','Terceiro']
print (lista)

#Invertendo uma lista
lista.reverse()
print (lista)

lista = ['Quarto','Terceiro','Segundo','Primeiro']

#Odenando uma lista
lista.sort()
print (lista)

#Percorrendo uma lista
for elemento in lista:
	print (elemento)
	if(elemento == 'Quarto'):
		print ('Achamos o',elemento,'elemento da lista')
