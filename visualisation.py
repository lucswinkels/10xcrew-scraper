import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# Importeer de database, hier moet databestand veranderd worden naar bestand wat verwerkt moet worden.
df = pd.read_excel('backpacks.xlsx')

# Print de database
print(df)

# Bereken de correlatiematrix
correlation_matrix = df.corr(method='pearson')

# Print de correlatiematrix
print(correlation_matrix)

# Exporteer de correlatiematrix naar Excel
correlation_matrix.to_excel('visualisatie.xlsx', sheet_name='visualisatie_3', index=False)

# 
