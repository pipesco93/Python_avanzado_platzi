import time

def fibo_gen(max_it):
    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2 , aux
            if max_it >= counter:
                yield aux
            else:
                raise StopIteration

if __name__ == '__mains__':
    max_it = int(input('Ingresa el numero entero máximo de iteraciones: '))

    fibonacci = fibo_gen(max_it)
    for elements in fibonacci:
        print(elements)
        time.sleep(0.3)