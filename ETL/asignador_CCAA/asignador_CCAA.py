import csv

# Leer archivo2.csv y crear un diccionario de mapeo ciudad -> comunidad autónoma
ciudad_to_comunidad = {}
with open('C:/Users/julsb/Desktop/PROYECTOS/MINDER/RAW_DATA/PRECIOS_SESIONES_RESEARCH/DAME_DOCTORALIA/Scripts/contador_pags/results/ciudades_a_iterar3.csv', mode='r', encoding='utf-8') as file2:
    reader = csv.DictReader(file2)
    for row in reader:
        ciudad_to_comunidad[row['ciudad']] = row['comunidad_autonoma']

# Leer archivo1.csv y agregar la columna de comunidad autónoma
with open('C:/Users/julsb/Desktop/PROYECTOS/MINDER/RAW_DATA/PRECIOS_SESIONES_RESEARCH/DAME_DOCTORALIA/csv_compilado_con_ciudades.csv', mode='r', encoding='utf-8') as file1, open('C:/Users/julsb/Desktop/PROYECTOS/MINDER/RAW_DATA/PRECIOS_SESIONES_RESEARCH/DAME_DOCTORALIA/Scripts/contador_pags/results/archivo3.csv', mode='w', newline='', encoding='utf-8') as file3:
    reader = csv.reader(file1)
    writer = csv.writer(file3)
    
    # Leer y escribir la cabecera (header) del archivo1.csv
    header = next(reader)
    header.append('comunidad_autonoma')
    writer.writerow(header)
    
    for row in reader:
        ciudad = row[-2]  # Penúltima columna es la ciudad
        comunidad_autonoma = ciudad_to_comunidad.get(ciudad, 'Desconocida')
        row.append(comunidad_autonoma)
        writer.writerow(row)
