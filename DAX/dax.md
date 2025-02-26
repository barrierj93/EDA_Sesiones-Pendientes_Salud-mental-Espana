* doctoralia.csv:

100k_Canarias = 
CALCULATE(
    (SUM(poblacion_INE[Total Psicólogos]) / SUM(poblacion_INE[Total])) * 100000,
    FILTER(poblacion_INE, poblacion_INE[Comunidades y Ciudades Autónomas] = "Canarias")
)



Precio Medio Canarias = 
CALCULATE(
    AVERAGE(doctoralia[Precio]), 
    FILTER(doctoralia, doctoralia[comunidad_autonoma] = "Canarias")
)



precio_avg = AVERAGE('doctoralia'[Precio])

precio_max = MAX('doctoralia'[Precio])

precio_mediana = MEDIAN('doctoralia'[Precio])

precio_min = MIN('doctoralia'[Precio])

Psic_100k_comunidad = 
DIVIDE(
    [Total_psic],
    SUM('poblacion_INE'[Comunidades y Ciudades Autónomas]),
    0
) * 100000



Psic_100k_pais = 
DIVIDE(
    [Total_psic], 
    SUM('poblacion_INE'[Total]) / 100000
)



Total_psicDoctoralia = COUNTROWS('doctoralia')


-----------

* psic_INE.csv:

Mediana Psicólogos 100k = 
MEDIANX(
    VALUES(Hoja1[ccaa]),
    DIVIDE(
        SUM(Hoja1[total]),
        SUM(Hoja1[poblacion])
    ) * 100000
)


Psi_100k = 
DIVIDE(
    SUM(Hoja1[total]), 
    SUM(Hoja1[poblacion])
) * 100000

-----------

* poblacion_INE.csv:

Psic_100k_INE = 
DIVIDE(
    SUM('poblacion_INE'[Total Psicólogos]), 
    SUM('poblacion_INE'[Total]) / 100000, 
    0
)

-----------

* salarios.csv:

Ambos_Sexos_2022 = 
CALCULATE(
    SUM('salarios'[Suma de Importe €]),
    'salarios'[sexo] = "Ambos sexos",
    'salarios'[Año] = 2022
)


hombres_2022 = 
CALCULATE(
    SUM('salarios'[Suma de Importe €]),
    'salarios'[sexo] = "Hombres",
    'salarios'[Año] = 2022
)


mujeres_2022 = 
CALCULATE(
    SUM('salarios'[Suma de Importe €]),
    'salarios'[sexo] = "Mujeres",
    'salarios'[Año] = 2022
) 


Salario Medio Canarias = 
CALCULATE(
    AVERAGE(salarios[Suma de Importe €]), 
    FILTER(salarios, salarios[Com_autonoma] = "Canarias" && salarios[Año] = MAX(salarios[Año]))
)