import requests
from bs4 import BeautifulSoup
import csv
import os

# Función para leer URLs desde un archivo .txt
def leer_urls(archivo_txt):
    with open(archivo_txt, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls

# Función para extraer la primera tabla con clase "tabla" de una URL
def extraer_tabla(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Asegura que la solicitud se realizó correctamente
        soup = BeautifulSoup(response.content, 'html.parser')
        # Encuentra la primera tabla con clase "tabla"
        tabla = soup.find('table')
        if tabla:
            # Extrae las filas de la tabla
            filas = tabla.find_all('tr')
            # Extrae los datos de cada celda
            datos = []
            for fila in filas:
                celdas = fila.find_all(['td', 'th'])
                datos.append([celda.get_text(strip=True) for celda in celdas])
            return datos
        else:
            print(f"No se encontró ninguna tabla con clase 'tabla' en {url}")
            return None
    except requests.RequestException as e:
        print(f"Error al conectar con {url}: {e}")
        return None

# Función para guardar los datos de la tabla en un archivo CSV
def guardar_csv(datos, nombre_archivo):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(datos)

def main():
    # Solicita la ruta del archivo de URLs y del directorio de destino
    archivo_urls = input("Introduce la ruta del archivo .txt con las URLs: ")
    directorio_destino = input("Introduce la ruta del directorio donde quieres guardar los archivos CSV: ")
    
    # Lee las URLs desde el archivo proporcionado
    urls = leer_urls(archivo_urls)
    
    # Comienza la numeración de archivos en 2008
    numero_archivo = 2008
    
    # Procesa cada URL
    for url in urls:
        print(f"Procesando {url}...")
        datos = extraer_tabla(url)
        if datos:
            # Define el nombre del archivo CSV
            nombre_csv = os.path.join(directorio_destino, f"tabla_boe{numero_archivo}.csv")
            # Guarda los datos en el archivo CSV
            guardar_csv(datos, nombre_csv)
            print(f"Tabla guardada en {nombre_csv}")
            numero_archivo += 1

if __name__ == "__main__":
    main()
