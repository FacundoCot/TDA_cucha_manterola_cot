def tiempo_minimo(rivales):
    rivales.sort(key=lambda rival: int(rival[1]), reverse=True)

    tiempo_scaloni = 0

    for tiempos in rivales:
        Si = int(tiempos[0])
        Ai = int(tiempos[1])

        tiempo_scaloni += Si
        fin_analisis = tiempo_scaloni + Ai

    return fin_analisis