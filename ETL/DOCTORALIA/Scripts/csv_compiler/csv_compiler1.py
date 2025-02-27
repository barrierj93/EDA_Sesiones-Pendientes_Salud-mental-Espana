import os
import pandas as pd

def combinar_csvs():
    # Solicitar las rutas al usuario
    ruta_entrada = input("Ingrese la ruta donde están los archivos CSV: ")
    ruta_salida = input("Ingrese la ruta donde quiere guardar el archivo combinado: ")
    nombre_archivo_salida = input("Ingrese el nombre del archivo CSV de salida (incluya .csv): ")
    
    # Lista para almacenar los DataFrames
    dataframes = []
    
    # Recorrer todos los archivos en el directorio de entrada
    for archivo in os.listdir(ruta_entrada):
        if archivo.endswith(".csv"):
            archivo_csv = os.path.join(ruta_entrada, archivo)
            df = pd.read_csv(archivo_csv)
            dataframes.append(df)
    
    # Concatenar todos los DataFrames
    df_combinado = pd.concat(dataframes, ignore_index=True)
    
    # Guardar el DataFrame combinado en el archivo de salida
    ruta_completa_salida = os.path.join(ruta_salida, nombre_archivo_salida)
    df_combinado.to_csv(ruta_completa_salida, index=False)
    
    print(f"Archivos CSV combinados guardados en: {ruta_completa_salida}")

if __name__ == "__main__":
    combinar_csvs()


