def mediana(vector):
    vector.sort()               # ordena la lista de valores
    index = len(vector) // 2      # para obtener un indice entero
    if len(vector) % 2 != 0:    # comprueba la longuitud de la lista es impar      
        return vector[index]
    return (vector[index-1] + vector[index]) / 2
