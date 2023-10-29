# 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

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
    
    
#3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.

def invertirNumero(a : int) -> int: #la funcion recibe un entero y retorna un entero
    invertido = 0 #variable para almacenar el numero invertido
    while a != 0: #condición de número diferente de cero para iniciar el ciclo
        invertido = 10*invertido+a % 10 #toma los digitos de atras hacia adelante
        a //= 10 #obtiene la division exacta sobre 10
    return invertido

if __name__== "__main__":
    a= int(input("ingrese un numero entero: "))
    b = int(input("ingrese un numero entero: "))
    invert = invertirNumero(a)
    if b == invert:
        print(str(a) + " y " + str(b) + " son números espejos")
    else:
        print(str(a) + " y " + str(b) + " no son números espejos")







#7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

def vocales(lista: list) -> list: #la entrada de la función es una lista y retorna una lista
    cadenaVocales = [] #lista vacía para guardar las cadenas con más de dos vocales
    for i in lista: #recorre todos los elementos de la lista
       vocal = [letra for letra in i if letra in "AEIOU" or letra in "aeiou"] #lista que guarda las vocales de un elemento de la lista
       if len(vocal) >= 2: #condición de más de dos repeticiones de vocales en el elemento
            cadenaVocales.append(i) #va agegando los elementos a la lista vacía
    if len(cadenaVocales) == 0: #condición de al menos un elemento en la lista cadenaVocales
        return("no esxiste") #si no hay elementos retorna "no existe"
    else:
        return cadenaVocales

if __name__ == "__main__":
    n = int(input("ingrese la cantidad de elementos para la lista: "))
    lista = [(input("ingrese un elemento: ")) for x in range(n)]
    elementosVocales = vocales(lista)
    print(elementosVocales)
