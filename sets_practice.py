#Esta es una practica con la estrutura de los sets

#Los sets son estructuras de datos que son inmutables y no tienen datos que se repiten

#Pasando de otro data type to a set

my_list = [1, 1, 2, 3, 4, 4, 5]
print(my_list)
my_set = set(my_list)
print(my_set)

my_tuple = ("Hola", "Hola", 1)
print(my_tuple)
my_set2 = set(my_tuple)
print(my_set2)

print("*"*80)
#Adding more items to the sets early created
my_set.add(4)
print(my_set)

my_set.update([1, 2, 5]) #Adding more that 1 item
print(my_set)

my_set.update({1, 7, 2}, {6, 8}) #Also you can add diferent types of items
print(my_set)

print("*"*80)
#How to erase items in a set
my_set = {1, 2, 3, 4, 5, 6, 7}
print(my_set)

my_set.discard(1)
print(my_set)

my_set.remove(2)
print(my_set)

my_set.discard(10) #you can try to remove a item and if the item dont exist in the set is fine
print(my_set)

print("*"*80)
#my_set.remove(12) -> this line will make a error

#Remove an a aletory item of the set
my_set.pop()

my_set.clear() #this method help to clear all the data in the set
print("*"*80)