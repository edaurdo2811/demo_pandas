import pandas as pd
import numpy as np 

df = pd.DataFrame()
chunks=pd.read_csv('all_data.csv',chunksize=100000,names=['producto','presentacion','marca','categoria','catalogo','precio','fechaRegistro','cadenaComercial','giro','nombreComercial','direccion','estado','municipio','latitud','longitud'])
df=pd.concat(chunk.groupby(['categoria','cadenaComercial','producto','estado']).size().reset_index(name="Categories") for chunk in chunks)

numReg = df['Categories'].sum()
print('-------> Se cuentan {} registros totales <--------\n'.format(numReg))

numcat = df['categoria'].nunique()
print('-------> Existen {} categorias <--------\n'.format(numcat))

numCadCom = df['cadenaComercial'].nunique()
print('-------> Existen {} cadenas que reportan <--------\n'.format(numCadCom))



df2 = df.groupby(['estado','producto']).size().reset_index().rename(columns={0: 'count_by_state'})
df3 = df2.groupby(['estado'])['producto','count_by_state'].max()

print('------------------------------> ****************************************** <------------------------------\n')
print('------------------------------> Tabla por estado, con productos y cantidad <------------------------------\n')
print('------------------------------> ****************************************** <------------------------------\n')
print(df3)
print('------------------------------> ****************************************** <------------------------------\n')
print('------------------------------> ****************************************** <------------------------------\n')

df5 = df.groupby(['cadenaComercial'])['producto'].count().sort_values(ascending=False).head(1)
print('-------> Cadena que reporta más productos:  <--------\n')
for index,value in df5.items():
  print(f"Cadena Comercial: {index} con {value} productos reportados")
print('-----------------------------------------------------\n')

#dtypes = {'precio':'int'}
#names=['producto','presentacion','marca','categoria','catalogo','precio','fechaRegistro','cadenaComercial','giro','nombreComercial','direccion','estado','municipio','latitud','longitud']
#chunks=pd.read_csv('all_data.csv',chunksize=100000,sep=',',header=0)
#dfTest = pd.DataFrame()
#dfTest=pd.concat(chunk.groupby(['producto','estado','precio','fechaRegistro']).size().reset_index(name="Categories") for chunk in chunks)
#dfTest.groupby('producto').agg({'fechaRegistro': ['min', 'max'], 'precio': ['min','max']})
