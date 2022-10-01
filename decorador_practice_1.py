#Este es el primer ejemplo del uso de decoradores

def decorador(func):

    def envoltura():
        print("Esto se agrega a la funcion original")
        func()
    
    return envoltura

@decorador
def saludo():
    print("Hola mundo")

saludo()