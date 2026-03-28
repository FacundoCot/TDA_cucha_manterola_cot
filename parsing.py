
def parsing(archivo):

    tiempos_rivales = []

    try:
        with open(archivo) as f:
            
            for linea in f:

                linea.strip()
                separada = linea.split(',')
                tiempo = (separada[0],separada[1])
                tiempos_rivales.append(tiempo)

            return tiempos_rivales[1:]

    except FileNotFoundError:

        print("error: archivo no encontrado")     
    
            

