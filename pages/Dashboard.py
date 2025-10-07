import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#------------ Lectura ------------ 
st.set_page_config(page_title="Dashboard", layout="wide")
st.title(" Dashboard de Datos")


url = "https://raw.githubusercontent.com/Kalbam/Datos_DATAVIZ/main/empleo_juvenil.csv"
df = pd.read_csv(url)


#------------ NA ------------ 

st.subheader("Vista previa de los datos:")
st.dataframe(df.head())
st.bar_chart(df["Departamento"].value_counts())

st.header("Resumen de valores nulos por columna")
na_count = df.isna().sum()
na_percent = (na_count / len(df)) * 100
na_df = pd.DataFrame({
    'Valores Nulos': na_count,
    'Porcentaje (%)': na_percent.round(2)
}).sort_values(by='Valores Nulos', ascending=False)
st.dataframe(na_df)

st.text("El dataset no contine valores NA, por lo que procederemos con el EDA")

#------------ EDA ------------ 

# --- RESUMEN DE VARIABLES NUMÉRICAS ---
st.subheader("Resumen de variables numéricas (Edad e Ingreso)")
resumen_num = df[['Edad', 'Ingreso']].describe().T
st.dataframe(resumen_num)
st.text("Las edades van de 18 a 27 años, con una media de 22.6 años y una desviación estándar de 2.9, lo que sugiere que la mayoría de las personas se encuentran en una franja relativamente homogénea (principalmente entre los 20 y 25 años).")
st.text("Los ingresos varían entre 7.353 y 1.993.095 unidades monetarias, con una media cercana a 943.555. La gran diferencia entre el mínimo y el máximo, junto con una desviación estándar alta (≈ 555.000), indica que hay bastante desigualdad en los ingresos. El 50% de las personas ganan menos de 932.000, mientras que el 25% gana más de 1.403.000, lo que sugiere una cola derecha (pocos ingresos muy altos).")

# --- RESUMEN DE VARIABLE CATEGÓRICA ---
st.subheader("Resumen de variable categórica (Ocupación)")
resumen_cat = df[['Ocupación']].describe().T
st.dataframe(resumen_cat)
st.text("La categoría más frecuente es “Trabajador”, que aparece 72 veces, lo que indica que representa el grupo laboral más común dentro del conjunto de datos.")

# --- BOXPLOT: Distribución de Edad por Ocupación ---
st.subheader("Distribución de Edad por Ocupación")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='Ocupación', y='Edad', ax=ax)
ax.set_title("Distribución de Edad por Ocupación")
plt.xticks(rotation=45)
st.pyplot(fig)
st.text("A partir del grafico anterior identificamos, que la concentración de los jovenes que trabajan dentro de nuestro rango de edad suele ser un poco mayor en comparación a los que estudian y los desempleados. Además que el punto medio para los estudiantes y trabajadores es el mismo. Sin embargo, las 3 categorías siguen una distribución similar siendo la de estudiante y desempleado las más similares ")
