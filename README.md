# Sesiones Pendientes: Salud Mental en España 

Recorrido por la accesibilidad a **Profesionales de Psicología** en España a través de datos de fuentes oficiales e investigación independiente.

![Sesiones Pendientes Dashboard](Sesiones-Pendientes.png)

## **Descripción del Proyecto**
**Análisis exploratorio y visualización de datos** sobre aspectos relativos a la situación actual del acceso útil a sesiones con profesionales de la psicología.  
Se han recopilado datos de diversas fuentes para estudiar una posible relación entre factores socioculturales, demográficos, logístico-técnicos y económicos con el objeto de estudio.

## **Fuentes de Datos**

### '📁 EDA_Sesiones-Pendientes_Salud-mental-Espana/data' para consultar Fuentes. 
- **INE (Instituto Nacional de Estadística)**
- **BOE (Boletín Oficial del Estado)**
- **Doctoralia** (web scraping): Información sobre profesionales del sector privado 
- **Encuesta "Sesiones Pendientes"**: Datos sobre **usuarios y profesionales del sector**



## **Objetos de Análisis**
✓ Posibles **brechas de acceso** a la atención psicológica en España.  
✓ Identificar tendencias regionales y demográficas.  
✓ Sector privado: tarifas por sesión y capacidad economica de la población.  
✓ Psicología, psiquiatría y sanidad pública.

## **Principales Insights**

📊 Importante **Brecha salarial** entre las CC.AA. y, a su vez, entre hombres y mujeres.   
📊 **16 de 17 CC.AA. tienen menos psicólogos por cada 100k habitantes que la media.**   
📊En la Comunidad de Madrid hay **184 psicólogos por cada 100k habitantes (1º)** | en otras comunidades hay menos de **30**.   
📊 **83% de los encuestados** afirman que no podrían pagar más de 50€ por sesión, pero **ninguna CC.AA.** tiene una media de tarifas inferior a esa cantidad.    
📊 **Canarias** es la comunidad con el **segundo salario más bajo** y la **segunda tarifa más alta** por sesión.    
📊 La Rioja y Andalucía también presentan una correlación negativa entre salario medio y tarifas.  
📊 **País Vasco** presenta la mejor correlación entre **salario medio alto** y **tarifa baja** por sesión. 



## **Tecnología**
🔹 **Python** | ```pandas```, ```beautifulSoup```, ```csv```     
🔹 **Power BI** | **DAX**   
🔹 **Visual Studio**   
🔹 **Google Forms**
🔹 **LibreOffice** 


## 📂 **Estructura del Proyecto**
```
📦 Sesiones-Pendientes
 ┣ 📂 data/     
 ┃ ┣ 📂 clean/   # Archivos de datos limpios
 ┃ ┣ 📂 raw/   # datasets originales, resultados de scraping y encuestas
 ┣ 📂 DAX/   # Cálculos para Power BI / Tableau
 ┣ 📂 ETL/  # Scripts de procesamiento de datos
 ┣ 📄 Sesiones-Pendientes.pbit  # Plantilla de Power BI
 ┣ 📄 Sesiones-Pendientes.pdf   # Reporte en PDF
 ┗ 📄 Sesiones-Pendientes.png   # Imagen del Dashboard
```

## **Descarga y Uso**
1️⃣ **Clona el repositorio**  
```bash
git clone https://github.com/barrierj93/Sesiones-Pendientes.git
```
2️⃣ **Abre el archivo en Power BI**  
3️⃣ **Explora los datos y visualizaciones**  


· Cualquier aporte es bienvenido ·






## 🏛 **Licencia**
📜 Este proyecto está bajo la **Licencia MIT** - Puedes usarlo libremente con atribución.

---
