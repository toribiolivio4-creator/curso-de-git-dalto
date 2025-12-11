#Ferrari es más exclusiva que Lamborghini

import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cons_ferrari = pd.read_csv("Proyecto_Final1/concesionarios_ferrari.csv")
cons_lamborghini = pd.read_csv("Proyecto_Final1/consecionarios_lamborghini.csv")

fab_ferrari = pd.read_csv("Proyecto_Final1/Ferrari_unidades_fabricadas.csv")
fab_lamborghini = pd.read_csv("Proyecto_Final1/Lamborghini_unidades_fabricadas.csv")

ven_ferrari = pd.read_csv("Proyecto_Final1/Ferrari_unidades_vendidas.csv")
ven_lamborghini = pd.read_csv("Proyecto_Final1/Lamborghini_unidades_vendidas.csv")

#----------------------------------------------------------------------------------------------------

#Cual de las dos marcas fabrica mas autos?

mas_fabricado_f = fab_ferrari['Unidades Fabricadas (Aprox.)'].sum()
print(f'Ferrari desde su creación hasta hoy, ha fabricado:  {mas_fabricado_f} autos')

print('--------------------------------------------------------------------------')
mas_fabricado_l = fab_lamborghini['Unidades Fabricadas (Aprox.)'].sum()
print(f'Lamborghini desde su creación hasta hoy, ha fabricado:  {mas_fabricado_l} autos')

print('---------------------------------------------------------------------------------')
#---------------------------------------------------------------------------------------------------

#Cuantas agencias oficiales tiene cada marca alrededor del mundo?
agencias_ferrari = cons_ferrari['Región'].count()
print(f'Ferrari tiene {agencias_ferrari} agencias al rededor del mundo')

print('-------------------------------------------------------------------------------------')

agencias_lamborghini = cons_lamborghini['Región'].count()
print(f'Lamborghini tiene {agencias_lamborghini} agencias al rededor del mundo')

print('----------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------------------

#Cuantos modelos han fabricado desde su creación cada una de las marcas?
cant_modelos_ferrari = fab_ferrari['Modelo'].count()
print(f'Ferrari ha fabricado {cant_modelos_ferrari} modelos en su historia')

print('-------------------------------------------------------------------------------------')

cant_modelos_lamborghini = fab_lamborghini['Modelo'].count()
print(f'Lamborghini ha fabricado {cant_modelos_lamborghini} modelos en su historia')

print('--------------------------------------------------------------------------------------------')

#---------------------------------------------------------------------------------------------------

#Analizamos la diferencia de fabricacion entre modelos de ambas marcas
vol_ferrari = fab_ferrari.groupby('Modelo')['Unidades Fabricadas (Aprox.)'].sum()
print(f'Producción Total de Ferrari por modelo: {vol_ferrari}')

print('------------------------------------------------------------------------------------------')

vol_lamborghini = fab_lamborghini.groupby('Modelo')['Unidades Fabricadas (Aprox.)'].sum()
print(f'Producción Total de Lamborghini por modelo: {vol_lamborghini}')

print('-------------------------------------------------------------------------------------------------')

#Grafico Volumen de Fabricacion de cada modelo de Ferrari
plt.figure(figsize=(12, 6))
vol_ferrari.plot( x='Periodo de produccion', kind='bar')
plt.title('Fabricacion de Ferrari')
plt.ylabel('Cantidad de unidades fabricadas')
plt.xlabel('Modelos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Grafico Volumen de Fabricacion de cada modelo de Lamborghini
plt.figure(figsize=(12, 6))
vol_lamborghini.plot( x='Periodo de produccion', kind='bar')
plt.title('Fabricacion de cada modelo de Lamborghni')
plt.ylabel('Unidades Fabricadas')
plt.xlabel('Modelos')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#------------------------------------------------------------------------------------------------------

#Analizamos la diferencia de autos vendidos entre ambas marcas desde su creación
ferrari_vendidos = ven_ferrari['Total de Entregas (Aprox.)'].sum()
print(f'En total Ferrari ha vendido {ferrari_vendidos} autos en su historia')
print('-------------------------------------------------------------------------------------------')

lamborghini_vendidos = ven_lamborghini['Unidades Entregadas (Aprox.)'].sum()
print(f'En total Lamborghini ha vendido {lamborghini_vendidos} autos en su historia')

#Grafico Volumen de Ventas de Ferrari
plt.figure(figsize=(0, 12))
ven_ferrari.plot( x='Año', kind='bar')
plt.title('Autos vendidos por Ferrari en su historia')
plt.ylabel('Cantidad de autos vendidos')
plt.xlabel('Año')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()

#Grafico Volumen de Ventas de Lamborghini
plt.figure(figsize=(0, 12))
ven_lamborghini.plot( x='Año', kind='bar')
plt.title('Autos vendidos por Lamborghini en su historia')
plt.ylabel('Cantidad de autos vendidos')
plt.xlabel('Año')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.show()