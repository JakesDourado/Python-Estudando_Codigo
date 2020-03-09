#Declarando uma lista para trabalhar como Fila
fila = ['Primeiro','Segundo','Terceiro']

#Adicionando um elemento na fila
fila.append('Quarto')
print (fila)

#Removendo um elemento da Fila (Primeiro a entrar Primeiro a sair)
elemento = fila.pop(0)
print ('O elemento [',elemento,'] saiu da fila!')

#Removendo um elemento da Fila (Primeiro a entrar Primeiro a sair)
elemento = fila.pop(0)
print ('O elemento [',elemento,'] saiu da fila!')

print ('Sobrou os elementos ',fila)