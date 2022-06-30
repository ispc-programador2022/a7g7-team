from itertools import combinations

def combinacionesSuma(lista):
    temp = combinations(lista,2)
    sumaTotal = 0
    for i in list(temp):
        sumaTotal = sumaTotal + i[0] + i[1]
    return(sumaTotal)
        

