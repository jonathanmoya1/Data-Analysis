#Tarea 2_Análisis de Datos con Python
#Estudiante: Jonathan Moya Quirós

import pandas as pd
import matplotlib.pyplot as plt

#---------------------------------------------
#CARGA
#---------------------------------------------

# Debe cargar a Python el archivo “hotel_bookings.csv” que contiene un total de 119390 registros
df = pd.read_csv('C:/Users/moyaj/Documents/BIG DATA/Análisis de Datos con Python/Semana 2/Tareas/hotel_bookings.csv')
print(df.head(20))

# Una vez que haya cargado el archivo valide que el dataframe contiene el total de registros y las respectivas columnas del archivo original.
print("Columnas del dataframe: ", df.columns)
print("Total de registros: ", {df.shape[0]})

#-----------------------------------------------
# LIMPIEZA
#-----------------------------------------------

# A continuación, se deben realizar la limpieza de los siguientes campos:
# Para el campo Children se debe eliminar la etiqueta ‘NA’ y sustituirla con un 0 (Cero).
df['children'] = df['children'].replace('N/A', 0)
df['children'] = df['children'].fillna(0)
print(df)

# Para el campo Meal se debe eliminar la etiqueta “Undefined” y sustituirla por “AA”
# Primero verifico que la columna tenga el valor de "Undefined", si existe el valor deberia dar un output "True"
existe = (df['meal']=='Undefined').any()
print(existe)
df['meal'] = df['meal'].replace('Undefined','AA')

# Con el mismo script para validar si existe el valor "Undefined" valido si se hizo el reemplazo correcto, si ya no existe el valor "Undefined" deberia dar un output "False"
existe = (df['meal']=='Undefined').any()
print(existe)

# Para el Campo Distribution_channel se debe eliminar la etiqueta “Undefined” y sustituirla por “Comercial”.
df['distribution_channel'] = df['distribution_channel'].replace('Undefined','comercial')
existeComecial = (df['distribution_channel']== 'comercial').any()
print(existeComecial)

# Compruebo que ya el valor "Undefined" no exista mas en la columna
if 'Undefined' in df['distribution_channel'].values:
    print("El valor existe")
else:
    print("El valor no existe")
# Compruebo que el valor "Comercial" si exista mas en la columna
if 'comercial' in df['distribution_channel'].values:
    print("El valor existe")
else:
    print("El valor no existe")

# Para el Campo Market_Segment se debe eliminar la etiqueta “Undefined” y sustituirla por “Comercial”.
df['market_segment'] = df['market_segment'].replace('Undefined','comercial')

# Para el Campo Agent se debe eliminar la etiqueta “Null” y sustituirla por 0 (Cero).
df['agent'] = df['agent'].replace('Null',0)
df['agent'] = df['agent'].fillna(0)


# Para el Campo Company se debe eliminar la etiqueta “Null” y sustituirla por 0 (Cero).
df['company'] = df['company'].replace('Null',0)
df['company'] = df['company'].fillna(0)

# Asegúrese que no queden columnas con valores nulos, indefinidos o incongruentes, de ser así elimine estos registros del dataframe. 
df = df.dropna()

# --------------------------------------------------
# TRANSFORMACION DE DATOS
# --------------------------------------------------

# Modificar el campo Children, Agent y Company para que ahora sea entero
# Se convierten los valores en tipo "int" para que sean entero
df['children'] = df['children'].astype(int)
df['agent'] = df['agent'].astype(int)
df['company'] = df['company'].astype(int)

# --------------------------------------------------
# NUEVO ARCHIVO CSV
# --------------------------------------------------
df.to_csv('C:/Users/moyaj/Documents/BIG DATA/Análisis de Datos con Python/Semana 2/Tareas/hotel_bookings_cleared.csv', index=True, encoding='utf-8')
print("El nuevo archivo csv limpio ha sido exportado al mismo directorio de este script de Python")
          
# --------------------------------------------------
# ANALISIS DE DATOS
# --------------------------------------------------

#Por último, obtenga los siguientes patrones que se pudieron presentar con los datos del hotel, puede utilizar herramientas de visualización para mostrar el resultado:
#Cantidad de reservaciones que se cancelaron y las que no por cada año.
# Se filtran únicamente las reservaciones no canceladas
df_no_canceladas = df[df['is_canceled'] == 0]

# Se agrupan los datos por año y estado de cancelación
reservas_por_año = (df.groupby(['arrival_date_year', 'is_canceled']).size().unstack())

# Visualización del resultado
reservas_por_año.plot(kind='bar')
plt.title("Reservaciones canceladas y no canceladas por año")
plt.xlabel("Año")
plt.ylabel("Cantidad de reservaciones")
plt.show()

#Cantidad de niños y bebes que estuvieron en las reservaciones que no se cancelaron.
# Se suman los campos children y babies
ninos_bebes = df_no_canceladas[['children', 'babies']].sum()

# Visualización del resultado
ninos_bebes.plot(kind='bar')
plt.title("Cantidad de niños y bebés en reservaciones no canceladas")
plt.ylabel("Cantidad")
plt.show()

#Cantidad de adultos que estuvieron según las reservaciones que no se cancelaron. 
# Se calcula el total de adultos
total_adultos = df_no_canceladas['adults'].sum()

# Visualización del resultado
plt.bar(['Adults'], [total_adultos])
plt.title("Cantidad de adultos en reservaciones no canceladas")
plt.ylabel("Cantidad")
plt.show()

#Cantidad de reservas por market_segment que no fueron canceladas.
# Se cuentan las reservaciones por segmento de mercado
reservas_market = df_no_canceladas['market_segment'].value_counts()

# Visualización del resultado
reservas_market.plot(kind='bar')
plt.title("Reservaciones no canceladas por Market Segment")
plt.xlabel("Market Segment")
plt.ylabel("Cantidad de reservaciones")
plt.show()












