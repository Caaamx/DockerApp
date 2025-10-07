import streamlit as st
from streamlit_option_menu import option_menu

# Configuración general de la app
st.set_page_config(page_title="Empleo Juvenil en Colombia", layout="wide")

# Barra lateral de navegación
with st.sidebar:
    selected = option_menu(
        "Menú Principal",
        ["Inicio", "Georreferenciación", "Dashboard"],
        icons=["house", "geo-alt", "bar-chart"],
        menu_icon="cast",
        default_index=0
    )

# Página de inicio
if selected == "Inicio":
    st.title("Análisis del Empleo Juvenil en Colombia")
    st.image("https://cdn.pixabay.com/photo/2016/11/29/04/17/people-1867706_1280.jpg", width='stretch')
    st.markdown("""
    El empleo juvenil es uno de los retos sociales y económicos más importantes en Colombia.  
    Esta aplicación busca **analizar y visualizar datos relacionados con la situación laboral de los jóvenes**, 
    explorando categorías como *empleados, desempleados y estudiantes*, junto con variables como la **edad** y los **ingresos** promedio.

    A través de diferentes visualizaciones interactivas, podrás:
    - Observar la distribución geográfica del empleo juvenil por departamento.  
    - Analizar tendencias en edad e ingresos según la situación laboral.  
    - Explorar dinámicamente los datos mediante filtros y mapas interactivos.

    El propósito es ofrecer una herramienta sencilla pero informativa para comprender mejor el panorama del empleo juvenil en el país. 
    """)

    st.image("https://cloudfront-us-east-1.images.arcpublishing.com/semana/GXAOPDDOSVC3ZONP4HH4XZ55XQ.jpg", width='stretch')
# Redirección a las otras páginas (asegúrate de que existan en la carpeta /pages)
elif selected == "Georreferenciación":
    st.switch_page("pages/Geo.py")

elif selected == "Dashboard":
    st.switch_page("pages/Dashboard.py")
