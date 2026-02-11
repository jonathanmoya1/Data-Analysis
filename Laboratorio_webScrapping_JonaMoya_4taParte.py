#Laboratorio Final Web Scrapping cuarta parte
#Estudiante Jonathan Moya

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv(r"C:\Users\moyaj\Documents\BIG DATA\Análisis de Datos con Python\Semana 4\lab_final_limpios.csv")

X = df[["Precio"]]

# Modelo predictivo (clustering)
kmeans = KMeans(n_clusters=3, random_state=0)
df["Cluster"] = kmeans.fit_predict(X)

# Visualización
plt.scatter(df.index, df["Precio"], c=df["Cluster"])
plt.xlabel("Producto")
plt.ylabel("Precio")
plt.title("Segmentación de productos por precio")
plt.show()
