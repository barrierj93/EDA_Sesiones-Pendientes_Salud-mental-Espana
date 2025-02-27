# Sesiones Pendientes: Salud Mental en España 

Un recorrido por la accesibilidad a **Atención Psicológica en España** a través de datos de fuentes oficiales e investigación independiente.

![Sesiones Pendientes Dashboard](Sesiones-Pendientes.png)

## **Descripción del Proyecto**
Este proyecto es un **análisis exploratorio y visualización de datos** sobre la situación actual de la atención psicológica en España.  
Se han recopilado datos de diversas fuentes para estudiar la relación entre los diversos factores socioculturales, demográficos, logístico-técnicos y económicos involucrados en la materia.

## **Fuentes de Datos**

### '📁 EDA_Sesiones-Pendientes_Salud-mental-Espana/data' para consultar Fuentes. 
- **INE (Instituto Nacional de Estadística)**
- **Doctoralia** (web scraping): Información sobre profesionales del sector privado 
- **Encuesta "Sesiones Pendientes"**: Datos sobre **usuarios y profesionales del sector**



## **Objetivos del Proyecto**
✓ Analizar la **brecha de acceso** a la atención psicológica en España.  
✓ Identificar las **desigualdades entre comunidades autónomas**.  
✓ Comparar **los precios de las sesiones** con los **ingresos promedio** de la población.  
✓ Reflexionar sobre el **impacto de los salarios y disponibilidad de profesionales** en el acceso a la salud mental.

## **Principales Insights**

📊 Importante **Brecha salarial** entre CC.AA. y entre hombres y mujeres.   
📊 **16 de 17 CC.AA. tienen menos psicólogos por cada 100k habitantes que la media.**   
📊Madrid tiene casi **184 psicólogos por cada 100k habitantes (1º)**, mientras que algunas comunidades tienen menos de **30**.   
📊 **83% de los encuestados** afirman que no pueden pagar más de 50€ por sesión, pero **ninguna comunidad autónoma** tiene una media de precios inferior a esa cantidad.    
📊 **Canarias** es la comunidad con el **segundo salario más bajo** y el **segundo precio más alto** por sesión.    
📊 La Rioja y Andalucía también presentan una correlación negativa salario-precio.  
📊 **País Vasco** presenta la mejor correlación entre **salario medio alto** y **precio de sesión bajo**. 



## **Tecnología**
🔹 **Python** | ```pandas```, ```beautifulSoup```, ```csv```     
🔹 **Power BI** | **DAX**   
🔹 **Visual Studio**     
🔹 **LibreOffice** 


## 📂 **Estructura del Proyecto**
```
📦 AA_GitHub_PowerBI
 ┣ 📂 clean/          # Archivos de datos limpios
 ┃ ┣ 📄 doctoralia.csv
 ┃ ┣ 📄 poblacion_INE_mod2.csv
 ┃ ┣ 📄 precio_deseado.csv
 ┃ ┣ 📄 psic_INE.csv
 ┃ ┣ 📄 salarios.csv
 ┣ 📂 DAX/                     # Cálculos en Power BI
 ┃ ┣ 📄 dax.md
 ┃ ┗ 📄 tableau.md
 ┣ 📂 ETL/                     # Scripts de procesamiento de datos
 ┃ ┣ 📂 asignador_CCAA/
 ┃ ┃ ┗ 📄 asignador_CCAA.py
 ┃ ┣ 📂 contador_pags/
 ┃ ┃ ┣ 📂 results/
 ┃ ┃ ┣ 📄 contador_pags.py
 ┃ ┃ ┗ 📄 modificar_contador.py
 ┃ ┗ 📂 csv_compiler/
 ┃ ┃ ┣ 📂 results/
 ┃ ┃ ┗ 📄 csv_compiler1.py
 ┣ 📂 scraping/                # Web Scraping con Python
 ┃ ┣ 📄 html_to_csv_WEB_con_ciudad.py
 ┃ ┣ 📄 iterador_html_to_csv_WEB.py
 ┃ ┣ 📄 ciao_duplicados.py
 ┃ ┗ 📄 html_to_csv3.py
 ┣ 📄 Sesiones-Pendientes.pbix  # Archivo de Power BI
 ┣ 📄 Sesiones-Pendientes.pdf   # Reporte en PDF
 ┗ 📄 Sesiones-Pendientes.png   # Imagen del Dashboard
```

## **Descarga y Uso**
1️⃣ **Clona el repositorio**  
```bash
git clone https://github.com/barrierj93/Sesiones-Pendientes.git
```
2️⃣ **Abre el archivo en Power BI o Tableau**  
3️⃣ **Explora los datos y visualizaciones**  


· Cualquier aporte es bienvenido ·






## 🏛 **Licencia**
📜 Este proyecto está bajo la **Licencia MIT** - Puedes usarlo libremente con atribución.

---
