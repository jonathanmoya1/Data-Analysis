#Laboratorio Final Web Scrapping tercera parte
#Estudiante Jonathan Moya

from pyspark import SparkConf, SparkContext
import csv

conf = SparkConf().setMaster("local").setAppName("LaboratorioBigData")
sc = SparkContext(conf=conf)

raw = (
    sc.textFile(r"C:\Users\moyaj\Documents\BIG DATA\Análisis de Datos con Python\Semana 4\lab_final_limpios.csv")
      .map(lambda x: list(csv.reader([x]))[0])
      .filter(lambda x: x[0] != "Producto")
)

# Convertir a diccionario
data = raw.map(lambda l: {
    "Producto": l[0],
    "Precio": float(l[1])
})

# Estadísticas
precios = data.map(lambda x: x["Precio"])

print("Precio máximo:", precios.max())
print("Precio mínimo:", precios.min())
print("Precio promedio:", precios.mean())
