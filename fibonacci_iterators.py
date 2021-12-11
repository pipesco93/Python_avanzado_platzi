"""La sucesión comienza con los números 0 y 1;2​ a partir de estos, «cada término es la 
suma de los dos anteriores», es la relación de recurrencia que la define.
0 1 1 2 3 5 8 13 21 34 ........."""

import time

class FiboIter():

    def __init__(self, max= 5):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            #self.n1 = self.n2
            #self.n2 = self.aux  esto lo puedo resumir en python con swapping como llas sigueinte slíneas
            self.n1 , self.n2 = self.n2, self.aux
            self.counter += 1
            if self.max  >= self.counter:
                return self.aux
            else:
                raise StopIteration


if __name__ == '__main__':
    """
    instanciar al iterador --> el iterador es una clase, instanciar
    es el acto de convertir a partir de los planos u na classe un objeto, 
    es decir, de FiboIter obtengo un objeto, creo un iterador que sse va a guardar
    en la variable fibonacci
    """
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.5)