import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim
from Consulta import Consulta
import sortCoordinates
import time

consulta = Consulta()

@st.cache_data(ttl=86400)
def obtener_coordenadas():
    return consulta.ejecutar_consulta()

geolocator = Nominatim(user_agent="my-app")

st.set_page_config(layout="wide")

st.write("<h1 style='color: red;'>TrafficAgent</h1>", unsafe_allow_html=True)

while True:
    coords = obtener_coordenadas()
    print(coords)
    print("_______________cordenadas limpias ______________")
    resultados, muestras_por_coordenada = sortCoordinates.procesar_coordenadas(coords)
    print(resultados)

    if resultados is not None:
        coordenadas = [f"{row[1]}, {row[0]}" for row in resultados]

        # Crear un DataFrame con las coordenadas y nombres de columna adecuados
        data = pd.DataFrame(
            {
                "LATITUDE": [float(coord.split(",")[0]) for coord in coordenadas],
                "LONGITUDE": [float(coord.split(",")[1]) for coord in coordenadas],
                "Numero de accidentes": muestras_por_coordenada,
            }
        )

        # Ordenar el DataFrame por el número de accidentes en orden descendente
        data = data.sort_values(by="Numero de accidentes", ascending=False)

        ubicaciones = []
        for coord in coordenadas:
            location = geolocator.reverse(coord, exactly_one=True)
            if location is not None:
                address = location.raw.get("address", {})
                ubicacion_completa = ", ".join(
                    [address.get("road", ""), address.get("city", ""), address.get("state", ""), address.get("country", "")]
                )
                ubicaciones.append(ubicacion_completa)
            else:
                ubicaciones.append("")
        data["Ubicación"] = ubicaciones

        st.title("Mayor concentración de accidentes reportados")
        st.map(data)

        st.subheader("Ubicaciones exactas:")
        st.dataframe(data, width=1000)  # Ajusta el valor de width para hacer la tabla más ancha

    else:
        st.write("No se encontraron resultados de la consulta.")

    time.sleep(86400)
