import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Pronóstico del tiempo para los siguientes días')
place = st.text_input('Lugar: ')
days = st.slider('Pronóstico del tiempo', min_value=1, max_value=5, help='Seleccione el número de días.')
option = st.selectbox('Seleccionar para ver',('Temperatura','Clima'))
st.subheader(f'{option} para los {days} siguientes días en {place}')

if place: 
    try:  # Se configura un try y un except para cuando no exista la ciudad.
        # Traer los datos de temperatura y cielo.
        filtered_data = get_data(place, days) # Comunicación con el script backend.

        if option == 'Temperatura':
            #Los datos que se encuentran en el diccionario extraido se divide para 10 
            #ya que no muestra bien los datos de temperatura (muestra en centenas y mas.)
            #Coloco en una lista lo que saco de un diccionario de los datos filtrados.
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            #Lo mismo se realiza para los días.
            dates = [dict['dt_txt'] for dict in filtered_data]
            # Crear el grafico de temperatura.
            figure = px.line(x=dates, y=temperatures, labels={'x':'Día', 'y':'Temperatura (C)'})
            st.plotly_chart(figure)

        if option == 'Clima':
            #Se genera un dict, ya que de la data que sale con la API, sale, Clear, Clouds, etc...
            #La idea es generar una {llave:valor} con lo que sale del conjunto de datos con la API
            #y las imágenes.
            images = {'Clear':'images/clear.png','Clouds':'images/cloud.png','Rain':'images/rain.png','Snow':'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            #Genero un lazo for para todas las condiciones que bote la lsita que trae la API.
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            print(dates)
            #Se presenta las imágenes en forma de 3 columnas.
            #Para esto, primero agrupamos las imagenes con 3 unidades.
            #Eso lo podemos realizar con la función range.
            print(list(range(0, len(image_paths)))) # imprimo lo que muestra la lista de rango de las imágenes.
            groups = [] # Genero una lista vacía para las agrupaciones de 3 elementos
            groups1 = [] # Genero una lista vacía para los días.
            #En el siguiente lazo for, agrupo con 3 elementos los elementos de las listas de imágenes y días.
            for i in range(0, len(image_paths), 3): 
                groups.append(image_paths[i:i+3])
                groups1.append(dates[i:i+3])
            print(groups) # Imprimo las listas para comprobar
            print(groups1) #Imprimo la lista para comprobar.
            # En el siguiente lazo, muestro las imágenes del clima y los días en forma de columna.
            for group, group1 in zip(groups, groups1):
                print(group)
                print(group1)
                cols = st.columns(3)
                for i in range(0, len(group)):
                    cols[i].image(group[i], width=100)
                    cols[i].text(group1[i])

    except:
        st.write('El lugar no existe en la Base de datos.')