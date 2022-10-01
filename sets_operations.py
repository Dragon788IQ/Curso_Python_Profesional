#Practice of the operations with sets

#Union, Unir dos sets obviando los items repetidos
my_set_1 = {2, 3, 4}
my_set_2 = {4, 5, 6}

my_set3 = my_set_1 | my_set_2 
print(my_set3)

print("+"*80)

#Interseccion, crea un set solo con los datos que se repiteb en ambos sets
my_set_1 = {2, 3, 4}
my_set_2 = {4, 5, 6}

my_set3 = my_set_1 & my_set_2
print(my_set3)
print("+"*80)

#Diferencia, Crea un set que solo contiene la diferencia de los items
my_set_1 = {2, 3, 4}
my_set_2 = {4, 5, 6}

my_set3 = my_set_1 - my_set_2
print(my_set3)

my_set3 = my_set_2 - my_set_1
print(my_set3)
print("+"*80)

#Diferencia simetrica, crea un set pero omite los items que estan en ambas listas
my_set_1 = {2, 3, 4}
my_set_2 = {4, 5, 6}

my_set3 = my_set_1 ^ my_set_2
print(my_set3)
print("+"*80)