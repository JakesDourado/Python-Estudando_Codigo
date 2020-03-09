'''
#Declarando uma String
nome = 'Felipe'

#Pegando o tamanho de uma String
print (len(nome))

#Acessando um elemento da String
print (nome[0])

#Fatiando uma String
print (nome[3:])

#Fatiando uma String
print (nome[:2])

#Fatiando uma String
print (nome[1:4])

#Verifica se um elemento esta presente
print ('e' in nome)

#Verifica se um elemento NAO esta presente
print ('z' not in nome)

#Declarando uma String
frase = 'Vamos aprender Python de verdade no Citi'

#Passar tudo para MAIUSCULO
frase_upper = frase.upper()
print (frase_upper)

#Passar tudo para minusculo
frase_lower = frase.lower()
print (frase_lower)

#Transformar um objeto em String
num = 123
print (str(123), type(num))

#Retorna False se a string contiver algum 
#caracter que nao seja letras
print ("abc".isalpha())  # True
print ("1fg".isalpha())  # False
print ("123".isalpha())  # False
print ("/+)".isalpha())  # False



#Declarando uma String
frase = 'Vamos aprender Python de verdade no Citi'
print (frase)

#Alterar um elemento da String
nova_frase = frase.replace('aprender', 'DOMINAR')
print (nova_frase)

#Contar quantas vezes um elemento especifico aparece na String
count = nova_frase.count('Python')
print ('A palavra Python aparece',count,'vez')

#Podemos achar em que posicao está certa letra ou palavra.
lugar = nova_frase.find('Python')
print ('A palavra Python esta na posicao',lugar)

#Separar uma string por espaco vazio
frase = nova_frase.split()
print (frase, type(frase))

#Separar uma string por caractecer especifico
frase = nova_frase.split('Python')
print (frase, type(frase))
'''

#Declarando uma String
frase = 'vamos aprender Python de verdade no Citi'

frase_cotada = frase.split('Python')
print (frase_cotada)

#Podemos juntar nossa string separada
frase_join = 'PYTHON AVANÇADO e'.join(frase_cotada)
print (frase_join)

#Vamos deixar apenas a primeira letra maiuscula
frase_capitalize = frase.lower().capitalize()
print (frase_capitalize)

#Vamos deixar as letras de cada palavra maiuscula
frase_title = frase.title()
print (frase_title)

#O que for maiusculo vira minusculo e vice-versa.
frase_swapcase = frase.swapcase()
print (frase_swapcase)