#Laboratorio 1
#Estudiante: Jonathan Moya Quiros


import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.walmart.co.cr/alimentos"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

productos = []
precios = []

items = soup.find_all("div", class_="vtex-product-summary-2-x-container")

for item in items:
    try:
        nombre = item.find("span", class_="vtex-product-summary-2-x-productBrand").text.strip()
        precio = item.find("span", class_="vtex-product-price-1-x-sellingPriceValue").text
        
        precio = float(
            precio.replace("₡", "").replace(",", "").strip()
        )

        productos.append(nombre)
        precios.append(precio)
    except:
        continue

df = pd.DataFrame({
    "Producto": productos,
    "Precio (CRC)": precios
})

# VALIDACIÓN CRÍTICA
if df.empty:
    print("No se extrajeron datos. La estructura HTML pudo cambiar.")
else:
    print("Producto más caro:")
    print(df.loc[df["Precio (CRC)"].idxmax()])

    print("\nProducto más barato:")
    print(df.loc[df["Precio (CRC)"].idxmin()])

    print("\nPrecio promedio:")
    print(df["Precio (CRC)"].mean())

    df.to_csv("Laboratorio_1.csv", index=False)
    print("\nArchivo Laboratorio_1.csv generado correctamente")
