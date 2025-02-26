# ELIMINA LINEAS DUPLICADAS EN UNA LISTA (.txt)

import os

def procesar_archivo():
    # Solicitar la ruta del archivo de entrada
    ruta_archivo = input("Ingresa la ruta del archivo txt: ").strip()

    # Verificar si el archivo existe
    if not os.path.isfile(ruta_archivo):
        print("El archivo no existe. Por favor, verifica la ruta e inténtalo de nuevo.")
        return

    # Leer el contenido del archivo y eliminar líneas duplicadas
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        lineas_sin_duplicados = list(dict.fromkeys(lineas))

    # Definir la ruta del archivo de salida
    directorio = os.path.dirname(ruta_archivo)
    nombre_archivo = os.path.basename(ruta_archivo)
    ruta_salida = os.path.join(directorio, f"sin_duplicados_{nombre_archivo}")

    # Escribir el contenido sin duplicados en el nuevo archivo
    with open(ruta_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.writelines(lineas_sin_duplicados)

    print(f"El archivo sin líneas duplicadas se ha guardado en: {ruta_salida}")

if __name__ == "__main__":
    procesar_archivo()
