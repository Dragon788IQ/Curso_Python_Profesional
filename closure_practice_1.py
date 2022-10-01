#Esta es una pratica rapida de como se estrucuturan los closure

def make_multiplier(x: int) -> float:

    def multiplier(n: int) -> float:
        return x * n 

    return multiplier

times10 = make_multiplier(10)
times4 = make_multiplier(4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))