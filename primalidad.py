def es_primo(numero: int):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if  numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    
    if es_primo(9):  #si resultado funcion es igual a true
        print('Es primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()