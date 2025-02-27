# lee una lista de terminos de busqueda (doctoralia) y
# solicita una URL base para iterar y contar el nro 
# de paginas de resultados que lanza cada termino
# anotando todo en un .csv de salida


import requests
from bs4 import BeautifulSoup
import csv

def obtener_numero_paginas(url):
    """
    Obtiene el número de páginas de resultados de una búsqueda dada la URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica que la solicitud sea exitosa
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encuentra la última página en el componente de paginación
        paginas_elemento = soup.select('li.page-item a')  # Selecciona todos los enlaces de la paginación
        
        if paginas_elemento:
            # Obtiene el texto del último enlace, que debería ser el número total de páginas
            return int(paginas_elemento[-2].text.strip())  # Utilizamos -2 porque el último suele ser "Siguiente"
        else:
            return 0
    except Exception as e:
        print(f"Error al obtener número de páginas de {url}: {e}")
        return 0

def main():
    # Pedir rutas de archivos y URL base al usuario
    ruta_terminos = input("Introduce la ruta del archivo de términos de búsqueda (txt): ")
    ruta_salida = input("Introduce la ruta del directorio de salida: ")
    nombre_archivo = input("Introduce el nombre del archivo de salida (sin extensión): ")
    url_base = input("Introduce la URL base de la búsqueda: ")

    # Leer términos de búsqueda desde el archivo
    with open(ruta_terminos, 'r', encoding='utf-8') as file:
        terminos_busqueda = [line.strip() for line in file.readlines()]

    # Crear o abrir el archivo CSV para escribir resultados
    ruta_csv = f"{ruta_salida}/{nombre_archivo}.csv"
    with open(ruta_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Termino de Busqueda', 'Numero de Paginas'])

        # Realizar la búsqueda para cada término y guardar el número de páginas
        for termino in terminos_busqueda:
            url_completa = f"{url_base}{termino}"
            numero_paginas = obtener_numero_paginas(url_completa)
            writer.writerow([termino, numero_paginas])
            print(f"Término '{termino}': {numero_paginas} páginas")

    print(f"El archivo CSV se ha guardado correctamente en: {ruta_csv}")

if __name__ == "__main__":
    main()
