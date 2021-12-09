from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # defino los parametros de la funcion de esta manera para que el decorador reciba cualquier numero de parametro
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time =  datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper # un decorador es un closure y la nested function debeb retornarse

@execution_time #asi decoro la funcion de abajo y contabilizo el tiempo
def random_func():
    for _ in range(1, 10000000): #Cuando hago un ciclo for y no me interesa el valor que estamos recorriendo el ciclo utilizo _
        pass

@execution_time # si no uso (*args, **kwargs) el decorador no sirve 
def suma(a: int, b: int) -> int: 
    print(a + b)


random_func()
suma(5, 5)