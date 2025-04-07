import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definir las coordenadas de las tiendas

tiendas={
    'Tienda A':(1,1),
    'Tienda B':(1,5),
    'Tienda C':(7,1),
    'Tienda D':(3,3),
    'Tienda E':(4,8)
}

#Convertir las coordenadas a un dataframe para facilitar el cálculo

df_tiendas=pd.DataFrame(tiendas).T
df_tiendas.columns=['X', 'Y']
print("coordenadas de las tiendas:")
print(df_tiendas)

# Inicializar un dataframe para almacenar las distancias 

distancias_eu=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

# Cálculos de las distancias

for i in df_tiendas.index:
    for j in df_tiendas.index:
        
        # Distancias Euclidiana
        
        distancias_eu.loc[i,j]=distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])
        
        # Distancia Manhattan
        
        distancias_mh.loc[i,j]=distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])
        
        # Distancia Chebyshev
        
        distancias_ch.loc[i,j]=distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j])
        
    # Mostrar los resultados
    
    print("\nDistancias Euclidianas entre las tiendas:")
    print(distancias_eu)
    print("\nDistancias Manhattan entre las tiendas:")
    print(distancias_mh)
    print("\nDistancias Chebysev entre las tiendas:")
    print(distancias_ch)
    
    
        