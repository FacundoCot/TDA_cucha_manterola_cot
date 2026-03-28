#! /usr/bin/python3

import analizar_rivales
import parsing
import sys

ERROR_PARAMETROS = "parametros mal pasados"


def main():

    if len(sys.argv) != 2:
        raise Exception(ERROR_PARAMETROS)
    
    rivales = parsing.parsing(sys.argv[1])

    tiempo_optimo = analizar_rivales.tiempo_minimo(rivales)
    print(f"Tiempo optimo para {len(rivales)}: {tiempo_optimo}")


if __name__ == "__main__":
    main()