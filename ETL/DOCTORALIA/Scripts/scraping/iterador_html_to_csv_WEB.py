import subprocess

def main():
    # Pedir al usuario la ruta del script que deseamos ejecutar
    script_path = input("Ingrese la ruta del script que desea ejecutar (script_1.py): ")
    
    # Pedir al usuario la ruta del directorio donde queremos guardar los resultados
    output_dir = input("Ingrese la ruta del directorio donde desea guardar los resultados: ")

    # Pedir al usuario la URL base sin el número de la página al final
    base_url = input("Ingrese la URL base sin el número de la página al final: ")

    # Pedir al usuario el número de iteraciones
    num_iterations = int(input("Ingrese el número de iteraciones: "))

    # Pedir al usuario por qué número queremos empezar a iterar
    start_page = int(input("Ingrese el número de página por el que desea empezar a iterar: "))

    # Iterar sobre el número de páginas especificadas
    for i in range(start_page, start_page + num_iterations):
        # Construir la URL completa con el número de página
        url = f"{base_url}{i}"

        # Construir el nombre del archivo CSV basado en el número de iteración
        csv_file_name = f"resultado_pagina_{i}"

        # Ejecutar script_1.py utilizando subprocess para cada iteración
        try:
            subprocess.run(
                ["python", script_path],  # Ejecuta el script_1.py
                input=f"{url}\n{output_dir}\n{csv_file_name}\n",  # Pasa los parámetros a script_1.py
                text=True,  # Permite pasar las entradas como texto
                check=True  # Lanza una excepción si hay un error
            )
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar el script para la página {i}: {e}")
            continue

    print("Proceso completado.")

if __name__ == "__main__":
    main()
