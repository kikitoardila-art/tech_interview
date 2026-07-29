import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Configuración de la página
st.set_page_config(
    page_title="Akila - Dashboard Comercial",
    page_icon="🏢",
    layout="wide"
)

# Cargar datos
@st.cache_data
def cargar_datos():
    ruta = 'apartamentos_akila.csv'
    if not os.path.exists(ruta):
        ruta = '../apartamentos_akila.csv'
    
    df = pd.read_csv(ruta)
    return df

df = cargar_datos()

# Título y encabezado
st.title("🏢 Akila · Dashboard Comercial y Velocidad de Ventas")
st.markdown("Visualización estratégica del estado de inventario residencial.")

# Filtros en la barra lateral
st.sidebar.header("Filtros de Búsqueda")
estado_filtro = st.sidebar.multiselect(
    "Estado del Inmueble",
    options=df['estado'].unique(),
    default=df['estado'].unique()
)

tipologia_filtro = st.sidebar.multiselect(
    "Tipología",
    options=df['tipo_apartamento'].unique(),
    default=df['tipo_apartamento'].unique()
)

# Filtrar DataFrame
df_filtrado = df[
    (df['estado'].isin(estado_filtro)) & 
    (df['tipo_apartamento'].isin(tipologia_filtro))
]

# Métricas Principales (KPIs)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Unidades", len(df_filtrado))
col2.metric("Disponibles", len(df_filtrado[df_filtrado['estado'] == 'Disponible']))
col3.metric("Vendidos", len(df_filtrado[df_filtrado['estado'] == 'Vendido']))
total_ventas = df_filtrado[df_filtrado['estado'] == 'Vendido']['precio_cop'].sum() if 'precio_cop' in df_filtrado.columns else 0
col4.metric("Valor Ventas (COP)", f"${total_ventas:,.0f}")

st.markdown("---")

# Gráficos interactivos
c1, c2 = st.columns(2)

with c1:
    st.subheader("Estado del Inventario")
    fig_pie = px.pie(
        df_filtrado, 
        names='estado', 
        title='Distribución de Unidades por Estado',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with c2:
    st.subheader("Inventario por Tipología")
    fig_bar = px.histogram(
        df_filtrado, 
        x='tipo_apartamento', 
        color='estado', 
        barmode='group',
        title='Unidades por Tipología y Estado',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# Tabla de Datos
st.subheader("Detalle del Inventario")
st.dataframe(df_filtrado, use_container_width=True)
