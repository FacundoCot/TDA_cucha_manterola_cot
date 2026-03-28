def tiempo_minimo(rivales):
    rivales.sort(key=lambda rival: rival[1], reverse=True)

    tiempo_scaloni = 0
    tiempo_total = 0

    for tiempos in rivales:
        Si = int(tiempos[0])
        Ai = int(tiempos[1])

        tiempo_scaloni += Si
        fin = tiempo_scaloni + Ai

        if fin > tiempo_total:
            tiempo_total = fin

    return tiempo_total