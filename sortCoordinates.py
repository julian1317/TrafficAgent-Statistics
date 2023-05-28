import numpy as np
from sklearn.cluster import DBSCAN

def procesar_coordenadas(coordenadas):
    coordenadas_np = np.array(coordenadas)

    epsilon = 0.001  # rango
    min_samples = 1  # número de muestras

    modelo = DBSCAN(eps=epsilon, min_samples=min_samples)
    modelo.fit(coordenadas_np)

    etiquetas = modelo.labels_

    indices_representativos = np.unique(etiquetas, return_index=True)[1]

    coordenadas_filtradas = coordenadas_np[indices_representativos]

    muestras_por_coordenada = np.bincount(etiquetas + 1)[1:]  # Cuenta las muestras por coordenada

    return coordenadas_filtradas, muestras_por_coordenada
