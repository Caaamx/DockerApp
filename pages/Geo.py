import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# -----------------------------
# CONFIGURACIÓN DE LA PÁGINA
# -----------------------------
st.title("Mapa de Ocupación, Edad e Ingresos")
st.markdown("Visualización geográfica filtrable por ocupación, edad e ingresos.")

# -----------------------------
# CARGA DE DATOS
# -----------------------------
# Reemplaza con tu dataset real si es necesario
url = "https://raw.githubusercontent.com/Kalbam/Datos_DATAVIZ/main/empleo_juvenil.csv"
df = pd.read_csv(url)

# Asegurarse de que las columnas necesarias existen
cols_necesarias = ["Departamento", "Latitud", "Longitud", "Ocupación", "Edad", "Ingreso"]
if not all(col in df.columns for col in cols_necesarias):
    st.error(f"El dataset debe contener las columnas: {', '.join(cols_necesarias)}")
    st.stop()

# -----------------------------
# FILTROS DINÁMICOS
# -----------------------------
st.sidebar.header("Filtros")

# Filtro por Ocupación
ocupaciones = df["Ocupación"].unique()
ocupacion_seleccionada = st.sidebar.selectbox("Selecciona Ocupación", options=ocupaciones)

# Filtro por Edad
edad_min, edad_max = int(df["Edad"].min()), int(df["Edad"].max())
rango_edad = st.sidebar.slider("Rango de Edad", min_value=edad_min, max_value=edad_max, value=(edad_min, edad_max))

# Filtro por Ingreso
ingreso_min, ingreso_max = int(df["Ingreso"].min()), int(df["Ingreso"].max())
rango_ingreso = st.sidebar.slider("Rango de Ingreso", min_value=ingreso_min, max_value=ingreso_max, value=(ingreso_min, ingreso_max))

# -----------------------------
# APLICAR FILTROS AL DATAFRAME
# -----------------------------
df_filtrado = df[
    (df["Ocupación"] == ocupacion_seleccionada) &
    (df["Edad"].between(rango_edad[0], rango_edad[1])) &
    (df["Ingreso"].between(rango_ingreso[0], rango_ingreso[1]))
]

st.markdown(f"**Registros filtrados:** {df_filtrado.shape[0]}")

# -----------------------------
# CREAR MAPA INTERACTIVO
# -----------------------------
if not df_filtrado.empty:
    # Centrar el mapa en la media de las coordenadas
    centro = [df_filtrado["Latitud"].mean(), df_filtrado["Longitud"].mean()]
    m = folium.Map(location=centro, zoom_start=6)

    # Añadir puntos al mapa
    for _, row in df_filtrado.iterrows():
        popup_info = f"""
        <b>Departamento:</b> {row['Departamento']}<br>
        <b>Ocupación:</b> {row['Ocupación']}<br>
        <b>Edad:</b> {row['Edad']}<br>
        <b>Ingreso:</b> {row['Ingreso']:,.0f}
        """
        folium.CircleMarker(
            location=[row["Latitud"], row["Longitud"]],
            radius=6,
            color="blue" if row["Ocupación"] == "Empleado" else "green" if row["Ocupación"] == "Estudiante" else "red",
            fill=True,
            fill_opacity=0.7,
            popup=popup_info
        ).add_to(m)

    # Mostrar el mapa en Streamlit
    st_folium(m, width=900, height=600)
else:
    st.warning(" No hay datos que coincidan con los filtros seleccionados.")
