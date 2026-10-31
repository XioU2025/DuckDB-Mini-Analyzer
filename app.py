import streamlit as st
import duckdb
import pandas as pd

st.set_page_config(
    page_title="DuckDB Mini Analyzer",
    page_icon="🦆"
)

st.title("🦆 DuckDB Mini Analyzer")
st.write("Analiza archivos CSV utilizando consultas SQL.")

# Archivo de ejemplo
datos = {
    "producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "cantidad": [2, 5, 3, 2],
    "total": [8000, 250, 450, 2400]
}

df = pd.DataFrame(datos)

# Conexión DuckDB
conexion = duckdb.connect(":memory:")

archivo = st.file_uploader("Carga tu archivo CSV", type=["csv"])

if archivo is not None:
    df = pd.read_csv(archivo)
    st.success("Archivo cargado correctamente.")

st.dataframe(df, use_container_width=True)

# Registrar datos en DuckDB
conexion.register("ventas", df)

consulta = st.text_area(
    "Escribe tu consulta:",
    value="SELECT * FROM ventas;"
)

if st.button("Ejecutar consulta"):
    try:
        resultado = conexion.execute(consulta).df()

        st.dataframe(resultado, use_container_width=True)

        st.success("Consulta ejecutada correctamente.")

    except Exception as error:
        st.error(f"Error en la consulta: {error}")

st.caption("Proyecto educativo desarrollado con Python, Streamlit y DuckDB.")
