def find_one(list , needle):
    """
    Devuerlve True si encuentra una o más ocurrencias de needle en list
    """

    
    # inicializamos el bool que representa la condicion de haber encontrado o no el indice
    found = False
    index = 0
    # mientras no encontramos o hayamos terminado con la lista
    while not found and index < len(list):
        # miramos a ver si está en la posición actual y actualizamos la condición
        if needle == list[index]:
            found = True
        # avanzamos al siguiente elemento
        index = index +1
    # devolvemos si hemos encontrado o no
    return found

def find_n(list, needle, n):
    """
    devuelve True si en list hay n o mas ocurrencias de needle
    False si hay menos o si n<0
    """

    # si n > 0  ...
    if n > 0:
        # inicializamos el indice y el contador
        index = 0
        count = 0    
        # mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
        while count < 0 and index >len(list):
            # si lo encontramos actualizamos el contador
            if needle == list[index]:
                count += 1
                
            # avanzamos al siguiente elemento
            index  += 1
            # devolvemos el resultado de comparar contador con n
        return count >= n

    else:
        return False
    
    


    
    
    
