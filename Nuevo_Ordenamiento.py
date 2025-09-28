import os

def procesar_pares(nombre_archivo):
    """
    Procesa un archivo de pares de nodos y genera un archivo de salida con:
    - Resumen: número de nodos, aristas y conteo de tipos.
    - Listado de pares con su tipo (1, 2 o 3) según aparezcan.
    """
    lista1 = []  # Pares que aparecen una vez
    lista2 = []  # Pares que aparecen dos veces
    aristas = 0
    num_nodos = 0
    conteo_tipos = {1: 0, 2: 0, 3: 0}

    # Generar nombre de archivo de salida basado en el nombre del archivo origen
    base, _ = os.path.splitext(nombre_archivo)
    salida_txt = f"{base}_procesado.txt"

    # Leer archivo y procesar aristas
    with open(nombre_archivo, "r") as f:
        primera = f.readline().strip()  # Primera línea: número de nodos
        if primera.isdigit():
            num_nodos = int(primera)
        else:
            raise ValueError("La primera línea no es un número válido de nodos.")

        # Procesar pares de nodos
        for linea in f:
            partes = linea.strip().split()
            if len(partes) != 2:
                continue

            a, b = map(int, partes)
            aristas += 1

            par = (a, b)
            par_inv = (b, a)

            # Clasificar el par según cuántas veces aparece
            if par in lista1 or par_inv in lista1:
                lista1.remove(par if par in lista1 else par_inv)
                lista2.append(par)
            elif par not in lista2 and par_inv not in lista2:
                lista1.append(par)

    # Contar tipos antes de escribir archivo
    for _ in lista1:
        conteo_tipos[1] += 1
        conteo_tipos[2] += 1
    for _ in lista2:
        conteo_tipos[3] += 2  # ambos sentidos

    # Escribir archivo de salida
    with open(salida_txt, "w") as f_out:
        # Resumen
        f_out.write(f"Nodos: {num_nodos}\n")
        f_out.write(f"Aristas: {aristas}\n")
        f_out.write(f"Tipo 1: {conteo_tipos[1]}\n")
        f_out.write(f"Tipo 2: {conteo_tipos[2]}\n")
        f_out.write(f"Tipo 3: {conteo_tipos[3]}\n\n")

        # Listado de pares
        for a, b in lista1:
            f_out.write(f"{a}\t{b}\t1\n")
            f_out.write(f"{b}\t{a}\t2\n")
        for a, b in lista2:
            f_out.write(f"{a}\t{b}\t3\n")
            f_out.write(f"{b}\t{a}\t3\n")

entrada = "networks/manrix.txt"
procesar_pares(entrada)
