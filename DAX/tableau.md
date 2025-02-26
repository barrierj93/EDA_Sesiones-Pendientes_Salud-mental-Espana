# 📌 Cálculos en Tableau (Calculated Fields)

## 🔹 doctoralia.csv

### 1️⃣ Psicólogos por 100k en Canarias
```tableau
100k_Canarias =
IF [Comunidades y Ciudades Autónomas] = "Canarias" THEN 
    (SUM([Total Psicólogos]) / SUM([Total])) * 100000
END
```

### 2️⃣ Precio Medio en Canarias
```tableau
Precio Medio Canarias =
{ FIXED : AVG(IF [comunidad_autonoma] = "Canarias" THEN [Precio] END) }
```

### 3️⃣ Precio Promedio en España
```tableau
precio_avg =
AVG([Precio])
```

### 4️⃣ Precio Máximo
```tableau
precio_max =
MAX([Precio])
```

### 5️⃣ Mediana de Precio
```tableau
precio_mediana =
MEDIAN([Precio])
```

### 6️⃣ Precio Mínimo
```tableau
precio_min =
MIN([Precio])
```

### 7️⃣ Psicólogos por 100k por Comunidad Autónoma
```tableau
Psic_100k_comunidad =
(SUM([Total Psicólogos]) / SUM([Total])) * 100000
```

### 8️⃣ Psicólogos por 100k a Nivel Nacional
```tableau
Psic_100k_pais =
(SUM([Total Psicólogos]) / SUM([Total])) * 100000
```

### 9️⃣ Total de Psicólogos Registrados en Doctoralia
```tableau
Total_psicDoctoralia =
COUNT([Identificación])
```

## 🔹 psic_INE.csv

### 🔟 Mediana de Psicólogos por cada 100k Habitantes
```tableau
Mediana Psicólogos 100k =
MEDIAN( (SUM([total]) / SUM([poblacion])) * 100000 )
```

### 1️⃣1️⃣ Ratio de Psicólogos por cada 100k Habitantes
```tableau
Psi_100k =
(SUM([total]) / SUM([poblacion])) * 100000
```

## 🔹 poblacion_INE.csv

### 1️⃣2️⃣ Psicólogos por 100k según el INE
```tableau
Psic_100k_INE =
(SUM([Total Psicólogos]) / SUM([Total])) * 100000
```

## 🔹 salarios.csv

### 1️⃣3️⃣ Salario Total (Ambos sexos) en 2022
```tableau
Ambos_Sexos_2022 =
{ FIXED [Com_autonoma] : SUM(IF [sexo] = "Ambos sexos" AND [Año] = 2022 THEN [Suma de Importe €] END) }
```

### 1️⃣4️⃣ Salario Total Hombres en 2022
```tableau
hombres_2022 =
{ FIXED [Com_autonoma] : SUM(IF [sexo] = "Hombres" AND [Año] = 2022 THEN [Suma de Importe €] END) }
```

### 1️⃣5️⃣ Salario Total Mujeres en 2022
```tableau
mujeres_2022 =
{ FIXED [Com_autonoma] : SUM(IF [sexo] = "Mujeres" AND [Año] = 2022 THEN [Suma de Importe €] END) }
```

### 1️⃣6️⃣ Salario Medio en Canarias
```tableau
Salario Medio Canarias =
{ FIXED : AVG(IF [Com_autonoma] = "Canarias" AND [Año] = {MAX([Año])} THEN [Suma de Importe €] END) }
```
