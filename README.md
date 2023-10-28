# Taller2-Code_Weaver

![Code WEaver](https://github.com/alejayz/Taller2-Code_Weaver/assets/124609988/46277566-5ff4-4286-90c5-8bb09c18e2fd)

## Integrante: *Yazney Alejandra Arenas Garrido*

**1.** Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

```python

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
```

**2.** Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

```python

import math
def separar(a : float) -> list: #la entrada de la función es un número flotante y retorna una lista
    d, e = math.modf(a) #separa la parte decimal y la parte entera del número
    print(e) #imprime la parte entera
    print(d) #imprime la parte decimal
    digitos = [int(i) for i in str(a) if i != "."] #convierte el número a una lista de todos los dígitos del número ingresado
    return digitos


if __name__ == "__main__":
    a = float(input("ingrese un numero: "))
    digitosNum = separar(a)
    print (digitosNum)
```

**3.** Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos.

```python

def invertir_numero(a : int) -> int: #la funcion recibe un entero y retorna un entero
    invertido = 0 #variable para almacenar el numero invertido
    while a != 0: #condición de número diferente de cero para iniciar el ciclo
        invertido = 10*invertido+a % 10 #toma los digitos de atras hacia adelante
        a //= 10 #obtiene la division exacta sobre 10
    return invertido

if __name__== "__main__":
    a= int(input("ingrese un numero entero: "))
    b = int(input("ingrese un numero entero: "))
    invert = invertir_numero(a)
    if b == invert:
        print(str(a) + " y " + str(b) + " son números espejos")
    else:
        print(str(a) + " y " + str(b) + " no son números espejos")

```

**4.** Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.

**5.** Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva.

**6.** Desarrollar un programa que determine si en una lista existen o no elementos repetidos.

```python

def elementRepetidos(lista: list) -> bool: #la entrada de la función es una lista y retorna un booleano
    for i in lista: #recorre todos los elementos de la lista
       if lista.count(i) > 1: #cuenta las repeticiones de los elementos de la lista
           return True #retorna True si hay repeticiones en la lista
       else:
           return False #retorna False si no hay repeticiones en la lista

if __name__ == "__main__":
    n = int(input("ingrese la cantidad de elementos para la lista: "))
    lista = [(input("ingrese un elemento: ")) for x in range(n)]
    elementosRepetidos = elementRepetidos(lista)
    print(lista)
    print(elementosRepetidos)
```

**7.** Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

```python

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
```

**8.** Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

```python

def difLista(listaA:list, listaB:list) -> list: # las entradas de la función serán las dos listas
    diferentes = [] #lista vacía para agregar los elementos diferentes
    for i in listaA: #recorre la primera lista
        if i not in listaB: #verifica qué elementos de la primera lista no están en la segunda
            diferentes.append(i) #agrega a la variable "diferentes" los elementos diferentes
    return diferentes


if __name__ == "__main__":
    listaA = []
    listaB = []
    n = int(input("ingrese la cantidad de elementos para la lista A: "))
    for x in range(n):
        a = input("Ingrese un elemento para la lista A: ")
        listaA.append(a)
    z = int(input("ingrese la cantidad de elementos para la lista B: "))
    for x in range(z):
        a = input("Ingrese un elemento para la lista B: ")
        listaB.append(a)
    elementDif = difLista(listaA, listaB)
    print (elementDif)
```

**9.** Resolver el punto 7 del taller 1 usando operaciones con vectores.

**10.** Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%).

