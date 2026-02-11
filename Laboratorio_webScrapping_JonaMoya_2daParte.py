#Laboratorio Final Web Scrapping segunda parte
#Estudiante Jonathan Moya

import pandas as pd

df = pd.read_csv(r"C:\Users\moyaj\Documents\BIG DATA\Análisis de Datos con Python\Semana 4\lab_final.csv")

# Seleccionar columnas necesarias
df = df[["Producto", "Precio"]]

# Eliminar valores nulos
df = df.dropna()

# Eliminar duplicados
df = df.drop_duplicates()

# Crear categoría por rango de precio
def categoria_precio(precio):
    if precio < 20:
        return "Bajo"
    elif precio < 40:
        return "Medio"
    else:
        return "Alto"

df["Categoria"] = df["Precio"].apply(categoria_precio)

df.to_csv(r"C:\Users\moyaj\Documents\BIG DATA\Análisis de Datos con Python\Semana 4\lab_final_limpios.csv", index=False)
print("Archivo lab_final_limpios.csv generado correctamente")
