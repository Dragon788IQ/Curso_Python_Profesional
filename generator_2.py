#Reto de los generadores de fibonacci con un limite 
def FiboGenerator(max):
    n1 = 0
    n2 = 1
    aux = 0
    counter = 0
    aux_loop = True
    while aux_loop == True:
        if aux < max:
            if counter == 0:
                counter += 1
                yield n1
            elif counter == 1:
                counter += 1
                yield n2
            else:
                aux = n1 + n2
                n1, n2 = n2, aux
                counter += 1
                yield aux
        else:
            aux_loop = False

if __name__ == "__main__":
    max = int(input("Cual es el maximo que quieres en la sucesion? "))
    fibonacci = FiboGenerator(max)
    for element in fibonacci:
        print(element)

