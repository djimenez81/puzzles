import numpy as np

def baseLatinSquare(n):
    latinSquare = np.zeros((n,n),dtype = int)
    for i in range(n):
        for j in range(n):
            latinSquare[i,j] = (i+j)%n + 1
    return latinSquare
