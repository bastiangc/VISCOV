#IMPORTAR LIBRERÍAS NECESARIAS
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Visualización de los datos COVID-19 Chile")
st.markdown("### Bienvenido al visualizador")

df=pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv"
)
#AGREGAREMOS DOS COLUMNAS

col1,col2=st.columns(2)

with col1:
    region=st.radio("Región",df.Region.unique())
    st.markdown("Su selección es: "+region)
with col2:
    categoria=st.radio("Categoría",df.Categoria.unique())
    st.markdown("Su selección es: "+categoria)


#ilocs=df.iloc[:,2:-1]    
super_filtro=df[(df.Region == region) & (df.Categoria==categoria)]
st.dataframe(super_filtro)
fig,ax=plt.subplots()
to_plot=super_filtro.iloc[:,2:-1]
#st.table(to_plot)

ax.plot(to_plot.T)
ax.set_title(region)
ax.set_ylabel(categoria)
ax.set_xlabel("Fecha")

xs=np.arange(0,super_filtro.shape[1]-2,30)
plt.xticks(xs,rotation=90)

st.pyplot(fig)

