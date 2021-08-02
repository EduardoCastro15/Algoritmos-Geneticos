import numpy as np
import random

v1 = np.array([1, 2, 3, 4, 5, 6])
v2 = np.array([10, 20, 30, 40, 50, 60])
def cxTwoPoint(ind1, ind2):
    #size = min(len(ind1), len(ind2))
    while True:
        cxpoint = random.randint(1, len(ind1) - 1)
        cxpoint2 = random.randint(1, len(ind2) - 1)
        if (cxpoint!=cxpoint2):
            break
    ind1[cxpoint:], ind2[cxpoint:] = ind2[cxpoint:].copy(), ind1[cxpoint:].copy()
    ind1[cxpoint2:], ind2[cxpoint2:] = ind2[cxpoint2:].copy(), ind1[cxpoint2:].copy()
    print("Punto de cruza 1: ", cxpoint)
    print("Punto de cruza 2: ", cxpoint2)
    return ind1, ind2

v3, v4 = cxTwoPoint(v1, v2)
 
print(v3)
print(v4)