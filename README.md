# Sesiones Pendientes: Salud Mental en España 

Recorrido por la accesibilidad a **Atención Psicológica en España** a través de datos de fuentes oficiales e investigación independiente.

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
2️⃣ **Abre el archivo en Power BI o Tableau**  
3️⃣ **Explora los datos y visualizaciones**  


· Cualquier aporte es bienvenido ·






## 🏛 **Licencia**
📜 Este proyecto está bajo la **Licencia MIT** - Puedes usarlo libremente con atribución.

---
