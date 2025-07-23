import pandas as pd

# Carrega o arquivo Excel
df = pd.read_excel("Notas_Matematica_3B.xlsx")

# Salva como CSV
df.to_csv("notas_matematica3B.csv", index=False)