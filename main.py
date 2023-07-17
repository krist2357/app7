import streamlit as st
import plotly.express as px
from backend import get_data

st.title('Pronostico del tiempo para los siguientes días')
place = st.text_input('Lugar: ')
days = st.slider('Pronostico del tiempo', min_value=1, max_value=5, help='Seleccione el número de días.')
option = st.selectbox('Select data to view',('Temperatura','Cielo'))
st.subheader(f'{option} para los {days} siguientes días en {place}')

if place:
    try:
        # Traer los datos de temperatura y cielo.
        filtered_data = get_data(place, days)

        if option == 'Temperatura':
            #Se divide para 10 ya que no muestra bien los datos de temperatura
            temperatures = [dict['main']['temp']/10 for dict in filtered_data]
            dates = [dict['dt_txt'] for dict in filtered_data]
            # Crear el grafico de temperatura.
            figure = px.line(x=dates, y=temperatures, labels={'x':'Date', 'y':'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Cielo':
            # se genera, ya que de la data que sale con la API, sale, Clear, Clouds, etc...
            images = {'Clear':'images/clear.png','Clouds':'images/cloud.png','Rain':'images/rain.png','Snow':'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            #Genero un lazo for para todas las condiciones que bote la lsita que trae la API.
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            # Una imagen por condición
            st.image(image_paths, width=115)
    except:
        st.write('El lugar no existe en la Base de datos.')