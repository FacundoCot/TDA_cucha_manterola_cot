import random 
import numpy as np


SEED = 12345
INICIO = 1
FIN = 100000
random.seed(SEED)

def generar_datos(n):

    
    tiempos = [(random.randint(INICIO, FIN), random.randint(INICIO,FIN)) for _ in range(n)]
    
    return (tiempos,)
