#Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.

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
