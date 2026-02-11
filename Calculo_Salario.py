#Calculo Salario 
#Tarea 1
#Analisis de Datos con Python
#Estudiante: Jonathan Moya Quiros


#Usé esta libreria para poder almacenar el nuevo archivo csv en el mismo directorio donde esta el script de python
import os 
import pandas as pd

nombre = ""
departamento = ""
mes = ""
salarioBruto = 0 
salarioNeto = 0
deduccion = 0.1433


nombre = input("Digite el nombre del colaborador: ")
departamento = input("Ingrese el departamento: ")
mes = input("Ingrese el mes actual: ")
salarioBruto = float(input("Ingrese el monto del salario bruto del colaborador: "))


deduccionSalarioBruto = round(float(salarioBruto*deduccion),2)
salarioNeto = round(float(salarioBruto-deduccionSalarioBruto),2)

data = {'Nombre':[nombre],
        'Departamento': [departamento],
        'Mes':[mes],
        'Salario Bruto': [salarioBruto],
        'Deduccion': [deduccionSalarioBruto],
        'Salario Neto': [salarioNeto]
        }

#Con este script creo un nuevo dataframe con las el array formado en la variable data
df = pd.DataFrame(data) 

#Uso este script para asegurar que el nuevo archivo csv vaya a ser guardado en el mismo directorio donde se encuentra el script de python
ruta_script = os.path.dirname(os.path.abspath(__file__))
ruta_csv = os.path.join(ruta_script, "salario.csv") 

archivo_existe = os.path.exists(ruta_csv)

# Guarda acumulando datos en lugar de sobrescribir sobre el mismo arcgivo csv. 
# *IMPORTANTE* Cerrar el archivo csv cada vez que se vaya a sobrescribir datos, ya que si está abierto, va a generar un error. 
df.to_csv(
    ruta_csv,
    mode="a",
    index=False,
    header=not archivo_existe
)


print("Estimado",nombre,", departamento de:",departamento, ", se le informa que se ha procesado su salario del mes de ", mes, "y se desglosa así: ", "\n-----Salario bruto: ",salarioBruto, "\n-----Deducciones: ",deduccionSalarioBruto, "\n-----Salario Neto: ",salarioNeto)

print("Los datos fueron exportados exitosamente a salario.csv")