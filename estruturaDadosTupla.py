#Declarando uma tupla
tupla_1 = (30, 'Outrubro', 1989)
print (tupla_1)

#Podemos declar uma tupla sem ()
tupla_2 = 30, 'Outrubro', 1989
print (tupla_2)

#Acessando um elemento na tupla
print (tupla_2[0])

#Tupla com um unico elemento
tupla_2 = 1, #Sim!Precisa colocar uma virgula ao fim
print (tupla_2)

#Tupla com um unico elemento
tupla_2 = (1,)

#NAO pode adicionar elementos em uma tupla
tupla_2.append('elemento')