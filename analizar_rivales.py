def orden_optimo(rivales):
    return sorted(rivales, key=lambda rival: int(rival[1]), reverse=True)
    
def tiempo_minimo(rivales):
    orden = orden_optimo(rivales)

    tiempo_scaloni = 0
    fin_maximo = 0

    for tiempos in orden:
        Si = int(tiempos[0])
        Ai = int(tiempos[1])

        tiempo_scaloni += Si
        fin_analisis = tiempo_scaloni + Ai

        if fin_analisis > fin_maximo:
            fin_maximo = fin_analisis

    return fin_maximo