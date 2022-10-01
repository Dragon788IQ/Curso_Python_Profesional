#Segunda practica del uso de decoradores

# def funcion decoradora( funcion a decorar ):
#   def funcion interna():
#       codigo de la funcion inferna
#   return funcion interna
#
#   @funcion decoradora
#   def funcion a decorar():
#       codigo de la funcion a decorar

def mayusculas(func):
    def envoltura(text):
        return func(text).upper()
    
    return envoltura

@mayusculas
def mensaje(nombre):
    return(f"{nombre}, Recibiste un mensaje")

def run():
    print(mensaje("Johann"))

if __name__ == "__main__":
    run()