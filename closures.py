# Hola 3 -> Hola Hola Hola
# Facundo 2 -Z Facundo Facundo

from typing_extensions import runtime


def make_repester_of(n): # funcion envolvente la que tienen la nested function
    def repeater(string): # nested function
        assert type(string) == str, "slo puedes usar cadenas"
        return string * n # closure qye trabaja con balor de scope suerio n
    return repeater # debo hacer return de la nested function

def run():
    repest_5 = make_repester_of(5)
    print(repest_5("Felipe"))

if __name__ == '__main__':
    run()
