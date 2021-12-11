class EvenNumber:
    
    """
    Clase que implementa un iterador de todos los números pares, o los números pares hasta un máximo."""

    def __init__(self,max=10):
        self.max = max
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result= self.num
            self.num += 2
            print(result)
            return result

        else:
            raise StopIteration

if __name__ == '__main__':

    evens = EvenNumber()

    for element in evens:
        print(element)
