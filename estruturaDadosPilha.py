#Declarando uma lista para trabalhar como Pilha
pilha = ['Primeiro','Segundo','Terceiro']

#Adicionando um elemento na pilha
pilha.append('Quarto')
print (pilha)

#Removendo um elemento da Pilha (Ultimo a entrar Primeiro a sair)
elemento = pilha.pop()
print ('O elemento [',elemento,'] saiu da pilha!')

#Removendo um elemento da Pilha (Ultimo a entrar Primeiro a sair)
elemento = pilha.pop()
print ('O elemento [',elemento,'] saiu da pilha!')

print ('Sobrou os elementos ',pilha)