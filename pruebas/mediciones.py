from concurrent.futures import ProcessPoolExecutor, as_completed
import time 
import os




def tiempo_en_correr(algoritmo, *argumentos):
    hora_inicio = time.time()
    algoritmo(*argumentos)

    return time.time() - hora_inicio

def tiempo_algoritmo(algoritmo, tamaños, generar_datos):
    futures = {}
    tiempo_totales = {i: 0 for i in tamaños}

    with ProcessPoolExecutor(max(1, (os.cpu_count() or 0) //4)) as p:
        for i in tamaños:
            for _ in range(10):
                futures[p.submit(tiempo_en_correr, algoritmo,*generar_datos(i))] = i

        for f in as_completed(futures):
            result = f.result()
            i = futures[f]
            tiempo_totales[i] += result

    return {s: t / 10 for s, t in tiempo_totales.items()}



        