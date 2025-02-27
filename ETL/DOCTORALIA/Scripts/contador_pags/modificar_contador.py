import csv

# Paths for the input and output files
input_file_path = "C:/Users/julsb/Desktop/PROYECTOS/MINDER/RAW_DATA/PRECIOS_SESIONES_RESEARCH/DAME_DOCTORALIA/Scripts/contador_pags/results/ciudades_comunidades.csv"  # Cambia esto a la ruta de tu archivo CSV
output_file_path = "C:/Users/julsb/Desktop/PROYECTOS/MINDER/RAW_DATA/PRECIOS_SESIONES_RESEARCH/DAME_DOCTORALIA/Scripts/contador_pags/results/ciudades_comunidades_mod.csv"  # Cambia esto a la ruta donde deseas guardar el archivo modificado

# Leer y procesar el archivo CSV
with open(input_file_path, mode='r', encoding='utf-8') as input_file:
    reader = csv.reader(input_file)
    rows = [row for row in reader]

# Escribir el contenido modificado a un nuevo archivo CSV
with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file)
    for row in rows:
        # Asegura que cada celda esté entre comillas simples
        modified_row = [f"'{cell}'" for cell in row]
        writer.writerow(modified_row)

print(f"Archivo CSV modificado guardado en: {output_file_path}")
