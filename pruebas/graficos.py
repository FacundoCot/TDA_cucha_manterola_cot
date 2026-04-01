from matplotlib import pyplot as plt
import seaborn as sns 
import numpy as np
import scipy as sp
from pruebas.mediciones import tiempo_algoritmo
from analizar_rivales import tiempo_minimo
from pruebas.generar_datos import generar_datos

def graficar_medicion():

    x = np.linspace(100, 10_000_00, 20 ).astype(int)
    resultados = tiempo_algoritmo(tiempo_minimo, x, lambda s: generar_datos(s))

    ax: plt.Axes
    fig, ax = plt.subplots()
    ax.plot(x, [resultados[i] for i in x], label="Medición")
    ax.set_title("Tiempo de medicion de Tiempos Minimos")
    ax.set_xlabel("Cantidad elementos en el Array")
    ax.set_ylabel("Tiempo de ejecución (s)")
    plt.show() 

if __name__ == "__main__":
    graficar_medicion()