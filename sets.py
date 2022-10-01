#Practica mas reto con ayuda de los sets

def remove_duplicates(some_list: list) ->list:
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_fast(some_list):
    return list(set(some_list))

def run():
    my_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(my_list))
    print(remove_fast(my_list))

if __name__ == "__main__":
    run()
