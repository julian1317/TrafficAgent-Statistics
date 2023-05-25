import numpy as np
from sklearn.cluster import DBSCAN

def ordenar_coordenadas(coordenadas):
    # Convertir a matriz numpy
    coordenadas_np = np.array(coordenadas)

    # Configuración del algoritmo DBSCAN
    epsilon = 0.001 # Radio de búsqueda
    min_samples = 1  # Mínimo número de muestras 

    # Crear el modelo DBSCAN
    modelo = DBSCAN(eps=epsilon, min_samples=min_samples)

    # Ajustar el modelo a los datos de coordenadas
    modelo.fit(coordenadas_np)

    # Obtener las etiquetas de los clusters asignados a cada punto
    etiquetas = modelo.labels_

    # Obtener los índices de los puntos más representativos de cada cluster
    indices_representativos = np.unique(etiquetas, return_index=True)[1]

    # Filtrar los puntos representativos y obtener los datos finales
    coordenadas_filtradas = coordenadas_np[indices_representativos]

    # Devolver las coordenadas ordenadas
    return coordenadas_filtradas