
from turtle import filling


def find_one(list , needle):
    """
    Devuerlve True si encuentra una o más ocurrencias de needle en list
    """
    return find_n(list, needle, 1)
    
   

def find_n(list, needle, n):
    """
    devuelve True si en list hay n o mas ocurrencias de needle
    False si hay menos o si n<0
    """

    # si n > 0  ...
    if n >= 0:
        # inicializamos el indice y el contador
        index = 0
        count = 0    
        # mientras no hayamos encontrado al elemento n veces o no hayamos terminado la lista...
        while count < n and index < len(list):
            # si lo encontramos actualizamos el contador
            if needle == list[index]:
                count += 1
                
            # avanzamos al siguiente elemento
            index  += 1
            # devolvemos el resultado de comparar contador con n
        return count >= n

    else:
        return False
        

def find_streak(list, needle, n):
    """
    Devuelve True si en list hay n o más needles seguidos
    False, para todo lo demás
    """
    # si n >= 0
    if n >= 0:
        #Inicializo el indice, el contador y el indicador de racha
        index = 0
        count = 0
        streak = False

        # Mientras no haya encontradoa n seguidos u la lista no se haya acabao....
        while count < n and index < len(list):
            # si lo encuentro, activo el indicado de rachas y actualizo el contador
            if needle == list[index]:
                streak = True
                count = count + 1
            else:
                # si no lo encuentro, desactivo el indicador de de racha y pongo a cero el contador
                streak = False
                count =0
            
            # avanzo al siguiente elemento
            index = index + 1
        
        # devolvemos el resultado de comparar el contador con n SIEMPRE Y CUANDO  estemos en racha
        return count >= n and streak
    else:
        # para valores de n < 0, no tiene sentido
        return False

def first_elements(list):
    """
    Devuelve los primeros valores de cada lista de la lista
    """
    return nth_elements(list, 0)

def nth_elements(list_of_lists, n):
    """
    Devuelve los enésimo valores de cada lista de la lista
    """
    # crear lista vacia
    lista_first_elements = []
    # Recorrer la lista
    for i in list_of_lists:
        # añadir el primera elemento de cada lista a lista creada
        lista_first_elements.append(i[n])
    # devolver la nueva lista
    return lista_first_elements

def transpose(matrix):
    """
    Recibe una lista de lista y lo convierte en una lista de lista transpuesta(poner las filas de una matriz como columnas)
    """
    # crear una nueva matriz 
    matrix_results = []  
    # recorremos el enésimo elemento de cada
    for i in range(len(matrix[0])):         
        # añadir la lista a la nueva matrix
        matrix_results.append(nth_elements(matrix, i) )
    # devolver la nueva matriz
    return matrix_results

def displace(list, distance, filler=None):
    if distance == 0:
        return list

    elif distance > 0 :
        filling = [filler] * distance
        res = filling + list
        res = res[:-distance]
        return res
    
    else:
        filling = [filler] * abs(distance)
        res = list + filling
        res = res[abs(distance):]
        return res


def displace_matrix(m, filler=None):
    d = []
    for i in range(len(m)):
        d.append(displace(m[i], i - 1 , filler))

    return d

def reverse_list(lista):
    return list(reversed(lista))

def reverse_matrix(matrix):
    rm = []
    for col in matrix:
        rm.append(reverse_list(col))
    return rm


    




    
    


    
    
    
