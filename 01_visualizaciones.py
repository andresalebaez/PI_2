import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Mi Primer KPI') #Titulo
st.subheader('Trabajo Practico Nº 2 - Data Science - Henry') #Subtitulo
st.markdown('***') # Texto (los asteriscos generan una linea que corta mi pagina)

# Como crear un filtro
if st.checkbox('Mostrar DF'): #Creamos un condicional con un nombre, con checkbox como condicional.
    st.dataframe(df_kpi) #Esta condicion desplega un dataframe.

if st.checkbox('Vista de datos (Head o Tail)'): #Condicional Checkbox-Head
    if st.button('Mostrar head'): #Se crea el condicional button "Mostrar head"
        st.write(df.head()) #Write nos devuelve el texto de df.head
    if st.button('Mostrar tail'): ##Se crea el condicional button "Mostrar tail"
        st.write(df.tail()) #Write nos devuelve el texto de df.tail

#Slider
precio_limite = st.slider('Definir precio máximo',0,4000,1500) 
#parametros: ("titulo", valor minimo, valor maximo, valor por defecto)

#Cuerpo de la funcion
fig = plt.figure(figsize=(6,4))  #Seleccion de figura
sns.scatterplot(x= 'price', y = 'points', data=df[df['price']<precio_limite]) #Cantidad de valores
st.pyplot(fig) #Mostrar el grafico