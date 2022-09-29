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


    
    
    """
    loop = True
    needle_pos = []
    while loop:
        for value in list:
            if value == needle:
               pos = list.index(value)
                needle_pos.append(pos)
                """
