# Taller2-Code_Weaver

![Code WEaver](https://github.com/alejayz/Taller2-Code_Weaver/assets/124609988/46277566-5ff4-4286-90c5-8bb09c18e2fd)

## Integrante: *Yazney Alejandra Arenas Garrido*

**1.** Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

Para el desarrollo de este programa se creó la función **def separarDigitos()** en la cual, primero se crea una lista vacía que, por medio de un bucle while que va separando los dígitos del número, almacena los dígitos en una lista desde el ultimo hasta el primero y luego con **digitosNum.reverse()** invirte los elementos para que en la lista que retorna la función, aparezcan los dígitos en el orden del número ingresado. 
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

En este caso, es necesario importar el módulo **math** para poder ejecutar la función **def separar()**, en la cual se utiliza la función **math.modf()** que permite separar la parte entera y la parte decimal de un número; por último se crea un lista que contiene los dígitos del número ingresado sin tomar en cuenta el punto decimal.
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

Para determinar si dos números ingresados por el usuario son espejos, se creó la función **def invertirNumero()** la cual contiene una variable, al inicio igual a 0, en la que con un ciclo while se separan los dígitos del primer número para invertirlos y tener como resultado el el primer numero de manera invertida. Teniendo el primer numero invertido, el segundo número ingresado se compara con éste.
```python

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

```


**6.** Desarrollar un programa que determine si en una lista existen o no elementos repetidos.

Inicialmente se crea la función **def elementRepetidos()** y utilizando un ciclo for se recorre la lista ingresada y con **lista.count()** se cuenta si algún elemento se repite dos veces o más dentro de la lista, si es así la función retorna **True**, de lo contrario retorna **False**.

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

Se creó la función **def vocales()**, en la que primero se tiene una lista vacía en la que se almacenarán los elementos que tengan dos o más vocales; con un ciclo for se recorre la lista y se crea una lista en la que se tienen en cuenta letra por letra cada uno de los elementos y luego con **len()** se verifica la cantidad de vocales de un elemento, si tiene dos o más se utiliza **cadenaVocales.append()** para agregar dichos elementos a la lista vacía inicial; después también utilizando **len()** se verifica si no hay ningún elemeto con dos o más vocales, si es así, la función retorna ""no existe"" o de lo contrario retorna la lista con los elementos con dos o más vocales.

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

El usuario ingresa dos listas y con la función **def difLista()** se comparan ambas listas. Primero se crea una lista vacía para almacenar los elementos diferentes en la primera lista compararda con la segunda; para ello, con un ciclo for se recorre la lista y utilizando **if** se pone la condición de comparar los elementos que no estén en la segunda lista y que sí se encuentren en la primera para que con **diferentes.append()**, estos elementos diferentes se almacenen en la lista vacía del principio. La función retorna la lista con elementos diferentes.
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


