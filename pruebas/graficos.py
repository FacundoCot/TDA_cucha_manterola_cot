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

    f = lambda x, v1, v2: v1 * x * np.log(x) + v2
    p_optimos, _ = sp.optimize.curve_fit(f, x,[resultados[i] for i in x])
    
    error_cuadratico = np.sum((p_optimos[0] * x * np.log(x) + p_optimos[1] - [resultados[i] for i in x])**2)

    print(f"El error cuadratico es de: {error_cuadratico}")

    ax: plt.Axes
    _, ax = plt.subplots()
    ax.plot(x, [resultados[i] for i in x], label="Medición")
    ax.plot(x, [p_optimos[0]* n * np.log(n) + p_optimos[1] for n in x], 'r--', label="Ajuste")
    ax.set_title("Tiempo de medicion de Tiempos Minimos")
    ax.set_xlabel("Cantidad elementos en el Array")
    ax.set_ylabel("Tiempo de ejecución (s)")
    ax.legend()
    ax.grid()
    plt.show()

if __name__ == "__main__":
    graficar_medicion()
