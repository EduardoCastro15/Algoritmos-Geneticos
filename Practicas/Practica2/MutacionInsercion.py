import numpy as np
import random

v1 = np.array([1, 2, 3, 4, 5, 6])
def mutacionInsercion(ind1):
    while True:
        inicio = random.randint(0, len(ind1) - 1)
        fin = random.randint(0, len(ind1) - 1)
        if (inicio!=fin):
            break
    print("Antes: ", v1)
    print("Punto inicial: ", inicio)
    print("Punto final: ", fin)
    diferencia = max(inicio, fin) - min(inicio, fin)
    if(inicio < fin):
        if(diferencia == 1):
            aux = ind1[inicio]
            ind1[inicio] = ind1[fin]
            ind1[fin] = aux
        else:
            aux = ind1[inicio]
            for i in range(inicio, fin+1):
                ind1[i] = ind1[i+1]
            ind1[fin] = aux
    else:
        if(diferencia == 1):
            aux = ind1[inicio]
            ind1[inicio] = ind1[fin]
            ind1[fin] = aux
        else:
            aux = ind1[inicio]
            for i in range(inicio, fin, -1):
                ind1[i] = ind1[i-1]
            ind1[fin] = aux
    return ind1

v2 = mutacionInsercion(v1)
 
print("Despues: ", v1)