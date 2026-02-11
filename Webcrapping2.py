from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Configurar navegador
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://adamchoi.co.uk/teamgoals/detailed")

wait = WebDriverWait(driver, 10)

# Click en "All matches"
all_matches = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'All matches')]"))
)
all_matches.click()

# Seleccionar país
country_dropdown = wait.until(
    EC.element_to_be_clickable((By.ID, "country"))
)
country_dropdown.click()

country_option = driver.find_element(By.XPATH, "//option[text()='Spain']")
country_option.click()

time.sleep(3)

# Extraer tabla
rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

data = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    data.append({
        "Fecha": cols[0].text,
        "Equipo Local": cols[1].text,
        "Equipo Visitante": cols[2].text,
        "Goles Local": int(cols[3].text),
        "Goles Visitante": int(cols[4].text)
    })

# Crear DataFrame
df = pd.DataFrame(data)

# Análisis de patrones
df["Total Goles"] = df["Goles Local"] + df["Goles Visitante"]

print("Promedio de goles por partido:", df["Total Goles"].mean())
print("Partido con más goles:")
print(df.loc[df["Total Goles"].idxmax()])

# Guardar CSV
df.to_csv("Laboratorio_2.csv", index=False)

print("Archivo Laboratorio_2.csv generado correctamente")

driver.quit()
