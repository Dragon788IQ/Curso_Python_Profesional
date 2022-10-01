#practica libre del uso de los decoradores
import time

# *args and **kwargs sirven para ignorar la cantidad de argumentos pasados a la funcion decordora

def time_count(func):
    def wrapper(*args, **kwargs):
        inicial_time = time.time()
        func(*args, **kwargs)
        print(f"La ejecucion tardo: {time.time() - inicial_time}")
    return wrapper


@time_count
def random_func():
    for _ in range(1, 10000000):
        pass

def run():
    random_func()

if __name__ == "__main__":
    run()