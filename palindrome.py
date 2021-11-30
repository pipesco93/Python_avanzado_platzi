def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower() #python diferencia mayusculas y minusculas
    return string == string[::-1] #Retorna la palabra alreves

def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()

