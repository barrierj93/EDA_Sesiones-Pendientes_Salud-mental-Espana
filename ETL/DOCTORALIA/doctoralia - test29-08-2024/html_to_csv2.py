# Este script LEE EL CONTENIDO DE UN ARCHIVO HTML LOCAL (busqueda en doctoralia) y guarda los resultados
# en el folder que le indiquemos en un archivo .csv


import csv
from bs4 import BeautifulSoup

# Función para extraer datos de los resultados
def extract_data_from_html(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    results = soup.find_all('div', class_='card card-shadow-1 mb-1')

    data = []
    for result in results:
        psychologist_info = {}
        
        # Identificación del psicólogo/clinica/centro
        name = result.get('data-doctor-name', '').strip()
        psychologist_info['Identificación'] = name
        
        # URL del perfil
        profile_url = result.get('data-doctor-url', '')
        psychologist_info['URL del perfil'] = profile_url
        
        # Especialidades
        specializations_tag = result.find('span', {'data-test-id': 'doctor-specializations'})
        if specializations_tag:
            specializations = specializations_tag.text.strip()
            psychologist_info['Especialidades'] = specializations
        
        # Subespecialidades (adicional)
        sub_specializations_tag = specializations_tag.find_next('span', class_='hide') if specializations_tag else None
        if sub_specializations_tag:
            sub_specializations = sub_specializations_tag.text.strip()
        else:
            sub_specializations = "No especificado"
        psychologist_info['Subespecialidades'] = sub_specializations
        
        # Precio (Buscar el primer precio disponible)
        price_tag = result.find('p', class_='m-0 text-nowrap font-weight-bold')
        if price_tag:
            price = price_tag.text.strip()
        else:
            price = "No especificado"
        psychologist_info['Precio'] = price

        data.append(psychologist_info)
    
    return data

# Función para escribir los datos en un archivo CSV
def write_data_to_csv(data, csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Identificación', 'Especialidades', 'Subespecialidades', 'URL del perfil', 'Precio'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    # Solicitar al usuario las rutas de archivos y nombres
    html_file_path = input("Ingrese la ruta del archivo HTML: ")
    output_dir = input("Ingrese la ruta donde desea guardar el archivo CSV: ")
    csv_file_name = input("Ingrese el nombre del archivo CSV (sin extensión .csv): ")

    # Crear la ruta completa para el archivo CSV
    csv_file_path = f"{output_dir}/{csv_file_name}.csv"

    # Extraer datos del archivo HTML
    data = extract_data_from_html(html_file_path)

    # Escribir datos en el archivo CSV
    write_data_to_csv(data, csv_file_path)

    print(f"Archivo CSV generado exitosamente en: {csv_file_path}")

if __name__ == "__main__":
    main()
