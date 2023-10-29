#Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

def separarDigitos(n : int) -> list: # la entrada de la función es un número entero
    digitos = [] #lista vacía para agregar los digitos del número
    while n >= 1: #condición de un número mayor a cero para continuar el ciclo
        digitos.append(n % 10) #va tomando el último dígito y lo va agregando a la lista vacía
        n //= 10 #obtiene la división exacta sobre 10
        digitosNum= digitos[:] #lista de digitos del ultimo al primero
        digitosNum.reverse() #invierte los elementos de la lista
    return digitosNum


if __name__ == "__main__":
    n = int(input("ingrese un numero: "))
    digitSeparados = separarDigitos(n)
    print (digitSeparados)