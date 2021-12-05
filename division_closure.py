def make_division_by(n):
    #This closure returns a function that returnsthe division of an x number by n'''
    assert type(n) == int, "solo puedes usar numeros enteros"
    def divided(x):
        assert type(n) == int, "solo puedes usar numeros enteros"
        return x / n # closure qye trabaja con balor de scope suerio n
    return divided # debo hacer return de la nested function

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))

    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__ == '__main__':
    run()
