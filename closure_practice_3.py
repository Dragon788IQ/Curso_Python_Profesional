#Reto usando los closure

def make_divider(n: int) -> float:

    def divider(x: int) -> float:
        assert n != 0, "No puedes divir por cero"
        return x/n
    
    return divider


def run():
    division_by_3 = make_divider(3)
    print(division_by_3(18))

    division_by_5 = make_divider(5)
    print(division_by_5(100))

    division_by_18 = make_divider(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()