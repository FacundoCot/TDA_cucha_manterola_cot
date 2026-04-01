import random 

SEED = 1234
INICIO = 1
FIN = 10000


def generar_datos(n):

    random.seed(SEED )
    tiempos = [(random.randint(INICIO, FIN), random.randint(INICIO,FIN)) for _ in range(n)]
    
    return (tiempos,)
