#Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

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