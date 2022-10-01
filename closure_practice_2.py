#La segunda practica del uso de los closure

def multipler_maker(n):

    def multiplier(string):
        assert type(string) == str, "Error tienes que especificar una cadena de caracteres"
        return string * n
    
    return multiplier

def run():
    times_5 = multipler_maker(5)
    print(times_5("3"))

if __name__ == "__main__":
    run()