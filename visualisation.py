import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# Importeer de database, hier moet gefilterd databestand veranderd worden naar bestand wat verwerkt moet worden.
df = pd.read_excel('backpacks.xlsx')

# Print de database
print(df)

# Bereken de correlatiematrix
correlation_matrix = df.corr(method='pearson')

# Print de correlatiematrix
print(correlation_matrix)

# Exporteer de correlatiematrix naar Excel
correlation_matrix.to_excel('visualisatie.xlsx', sheet_name='visualisatie_3', index=False)

#  tabel organische positie vs backlinks
x_data= df['Position']
y_data= df['Backlinks']

plt.scatter(x_data, y_data)

plt.title('Organische positie vs Backlinks')
plt.xlabel('Organische positie')
plt.ylabel('Backlinks')

plt.show()

#  tabel organische positie vs UR
x_data= df['Position']
y_data= df['UR']

plt.scatter(x_data, y_data)

plt.title('Organische positie vs UR ')
plt.xlabel('Organische positie')
plt.ylabel('UR')

plt.show()

#  tabel organische positie vs Traffic
x_data= df['Position']
y_data= df['traffic']

plt.scatter(x_data, y_data)

plt.title('Organische positie vs Traffic')
plt.xlabel('Organische positie')
plt.ylabel('Traffic')

plt.show()