def make_division_by(n): '''This closure returns a function that returns
                            the division of an x number by n'''
    assert n.isnumeric(), "solo puedes usar numeros"
    def divided(x): # nested function
        assert x.isnumeric(), "solo puedes usar numeros"
        return x / n # closure qye trabaja con balor de scope suerio n
    return repeater # debo hacer return de la nested function

def run():
    repest_5 = make_repester_of(5)
    print(repest_5("Felipe"))

if __name__ == '__main__':
    run()
