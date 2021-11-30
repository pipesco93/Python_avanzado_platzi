def make_multiplier(x): #scope superior

    def multiplier(n): #nested function
        return x * n   #x variable de scope superior
 
    return multiplier  #Retorno multiplier la nested function 

times10 = make_multiplier(10) #crea una funcion make_multiplier qu recuerda al valor x como 10
times4 = make_multiplier(4)

print(times10(3)) # el 3 va a ser el n que paso de parámetro paea multiplier la nested function 
print(times4(5))
print(times10(times4(2)))

# los closures parecen en clases cortas para hacerlas mas elegantes y cuando estoy usando decoradores
