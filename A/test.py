import random
import randomNumberGenerator
import combinacionesSuma
import mediaVector
import medianaVector

numeros = randomNumberGenerator.genrnd()
print(numeros)
print("La suma de todas las combinaciones posibles es ",combinacionesSuma.combinacionesSuma(numeros))
print("El valor promedio del vector es ",mediaVector.mediaVector(numeros))
print("La mediana del vector es ",medianaVector.mediana(numeros)) 
