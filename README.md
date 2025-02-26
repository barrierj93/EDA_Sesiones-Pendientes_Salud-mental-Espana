# 🧠 Sesiones Pendientes: Salud Mental en España

**Un recorrido de datos sobre la accesibilidad a Atención Psicológica en España a través de datos del INE, Doctoralia y una encuesta de usuarios.**

![Sesiones Pendientes Dashboard](Sesiones-Pendientes.png)

## 📌 **Descripción del Proyecto**
Este proyecto es un **análisis exploratorio y visualización de datos** sobre la situación actual de la atención psicológica en España.  
Se han recopilado datos de diversas fuentes para estudiar la relación entre **salarios, número de profesionales y precios de sesiones** en cada comunidad autónoma.

## 📁 **Fuentes de Datos**
Los datos utilizados provienen de tres fuentes principales:
- **INE (Instituto Nacional de Estadística)**: Estadísticas sobre **salarios**, **población** y **número de psicólogos colegiados**.
- **Doctoralia**: Información sobre **precios de sesiones** y **cantidad de profesionales registrados en la plataforma**.
- **Encuesta "Sesiones Pendientes"**: Datos sobre la **capacidad económica de los usuarios** para pagar sesiones de psicología.

## 🎯 **Objetivos del Proyecto**
✔️ Analizar la **brecha de acceso** a la atención psicológica en España.  
✔️ Identificar las **desigualdades entre comunidades autónomas**.  
✔️ Comparar **los precios de las sesiones** con los **ingresos promedio** de la población.  
✔️ Reflexionar sobre el **impacto de los salarios y disponibilidad de profesionales** en el acceso a la salud mental.

## 📊 **Principales Insights**
🔹 **Canarias** es la **segunda comunidad con el salario más bajo** y el **segundo precio más alto** por sesión.  
🔹 **Madrid** tiene los precios más altos pero la mayor concentración de profesionales.  
🔹 **83% de los encuestados** afirman que no pueden pagar más de 50€ por sesión, pero **ninguna comunidad autónoma** tiene una media de precios inferior a esa cantidad.  
🔹 **País Vasco** presenta la mejor correlación entre **salario medio alto** y **precio de sesión bajo**.  
🔹 La disponibilidad de psicólogos es **desigual en España**: Madrid tiene casi **184 psicólogos por cada 100k habitantes**, mientras que algunas comunidades tienen menos de **30**.

## 🛠 **Tecnologías Utilizadas**
- **Power BI** y **Tableau** para la visualización de datos.
- **DAX y Tableau Calculated Fields** para el procesamiento de métricas.
- **Python** para **ETL y Web Scraping**.
- **Excel** y **CSV** para el manejo de datos.

## 📂 **Estructura del Proyecto**
```
📦 AA_GitHub_PowerBI
 ┣ 📂 clean_datasets/          # Archivos de datos limpios
 ┃ ┣ 📄 doctoralia.csv
 ┃ ┣ 📄 doctoralia.xlsx
 ┃ ┣ 📄 poblacion_INE_mod2.csv
 ┃ ┣ 📄 poblacion_INE_mod2.xlsx
 ┃ ┣ 📄 precio_deseado.csv
 ┃ ┣ 📄 precio_deseado.xlsx
 ┃ ┣ 📄 psic_INE.csv
 ┃ ┣ 📄 psic_INE.xlsx
 ┃ ┣ 📄 salarios.csv
 ┃ ┗ 📄 salarios.xlsx
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

## 📥 **Descarga y Uso**
1️⃣ **Clona el repositorio**  
```bash
git clone https://github.com/barrierj93/Sesiones-Pendientes.git
```
2️⃣ **Abre el archivo en Power BI o Tableau**  
3️⃣ **Explora los datos y visualizaciones**  

## 🤝 **Contribución**
¡Cualquier aporte es bienvenido! Si tienes ideas para mejorar el análisis o nuevas fuentes de datos, puedes abrir un **issue** o hacer un **pull request**.




# **¿El acceso a la atención psicológica debería ser un derecho o un privilegio?**  
Este análisis busca generar conciencia sobre las barreras económicas que existen en el acceso a la salud mental.  

📢 **Comparte este proyecto y contribuyamos al debate.**

## 🏛 **Licencia**
📜 Este proyecto está bajo la **Licencia MIT** - Puedes usarlo libremente con atribución.

---
