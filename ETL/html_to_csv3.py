# SOLICITA una URL y LEE EL CONTENIDO HTML (busqueda en doctoralia) 
# GUARDA los resultados en el folder que le indiquemos en un archivo .csv


import csv
import requests
from bs4 import BeautifulSoup

# Función para extraer datos de los resultados
def extract_data_from_html(html_content):
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
    # Solicitar al usuario la URL y los detalles del archivo CSV
    url = input("Ingrese la URL de la página web: ")
    output_dir = input("Ingrese la ruta donde desea guardar el archivo CSV: ")
    csv_file_name = input("Ingrese el nombre del archivo CSV (sin extensión .csv): ")

    # Crear la ruta completa para el archivo CSV
    csv_file_path = f"{output_dir}/{csv_file_name}.csv"

    # Obtener el contenido HTML de la URL
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el HTML de la URL: {e}")
        return

    # Extraer datos del contenido HTML
    data = extract_data_from_html(html_content)

    # Escribir datos en el archivo CSV
    write_data_to_csv(data, csv_file_path)

    print(f"Archivo CSV generado exitosamente en: {csv_file_path}")

if __name__ == "__main__":
    main()
