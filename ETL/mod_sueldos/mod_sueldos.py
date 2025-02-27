import pandas as pd

# Ruta del archivo de entrada (cambia esto por la ruta local de tu archivo)
input_file_path = "C:/Users/julsb/Desktop/PROYECTOS/Data_Science/Social/MINDER/RAW_DATA/DATA_EXTERNA/sueldos_spain/mod_sueldos/sueldos_año_CCAA_sexo.xlsx"

# Ruta del archivo de salida (cambia esto según donde desees guardar el archivo transformado)
output_file_path = "C:/Users/julsb/Desktop/PROYECTOS/Data_Science/Social/MINDER/RAW_DATA/DATA_EXTERNA/sueldos_spain/mod_sueldos/sueldos_transformados.xlsx"

# Leer el archivo Excel
data = pd.read_excel(input_file_path)

# Transformar los datos al formato solicitado
melted_data = pd.melt(
    data,
    id_vars=["Año", "Com_Autonoma"],  # Columnas que se mantienen
    value_vars=["Ambos sexos", "Mujeres", "Hombres"],  # Columnas a transformar
    var_name="sexo",  # Nombre para la nueva columna que indica el sexo
    value_name="Importe €",  # Nombre para la columna de valores
)

# Renombrar columnas para que coincidan exactamente con el formato solicitado
melted_data.rename(columns={"Com_Autonoma": "Com_autonoma"}, inplace=True)

# Guardar el archivo transformado
melted_data.to_excel(output_file_path, index=False)

print(f"Archivo transformado guardado en: {output_file_path}")
