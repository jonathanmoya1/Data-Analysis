#Laboratorio Final Web Scrapping primera parte
#Estudiante Jonathan Moya 

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

productos = []
precios = []

items = soup.find_all("article", class_="product_pod")

for item in items:
    nombre = item.h3.a["title"]
    precio = item.find("p", class_="price_color").text
    precio = precio.replace("£", "").replace("Â", "")
    precio = float(precio)


    productos.append(nombre)
    precios.append(precio)

df = pd.DataFrame({
    "Producto": productos,
    "Precio": precios
})

df.to_csv(r"C:\Users\moyaj\Documents\BIG DATA\Análisis de Datos con Python\Semana 4\lab_final.csv", index=False)
print("Archivo lab_final.csv generado correctamente")
