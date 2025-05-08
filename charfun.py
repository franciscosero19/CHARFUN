# Definición de la función esPalindromo

def esPalindromo(a):

    frase = []
    frase_inv = []

    # La frase se trata como una lista, se recorren sus elementos, y
    # se agregan a la lista "frase" únicamente las letras, trasnformadas
    # a minúsculas. De manera adicional, se crea una lista invertida

    for elem in list(a):
        if elem.isalpha() == True:
            frase.append(elem.lower())
            frase_inv.insert(0, elem.lower())

    # Si las listas están vacías, porque no se ha agregado ningún caracter, devolverá False

    if not frase or not frase_inv:
        return False

    # Si amabas listas son idénticas, la función devolverá True

    elif frase == frase_inv:
        return True

    # De lo contrario devolverá False

    else:
        return False
    

# Inicio del programa
     
if __name__ == "__main__":
    
    a = str(input("Introduzca la frase que desea comprobar: "))

    # Comprobación de que la frase introducida es un palíndormo

    if esPalindromo(a) == True:
        print("¡Es un palíndromo!")

    else:
        print("No es un palíndormo...")