#Practica de tapiado statico con python 

import numbers


def prim_number(number: int):
    result_list = [x for x in range(2, number+1) if number % x == 0 ]
    result_list = len(result_list) == 1
    if result_list == True:
        print(number, "Es un numero primo")
    else:
        print(number, "No es un numeor primo")

def run():
    input_x = input("Ingrese un numero ")
    number : int = int(input_x)
    print(prim_number(number))

if __name__ == "__main__":
    run()