import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the next days')
place = st.text_input('Place: ')
days = st.slider('Forescats Days', min_value=1, max_value=5, help='Select the number the forecast days')
option = st.selectbox('Select data to view',('Temperature','Sky'))
st.subheader(f'{option} for the next {days} days in {place}')

# genero  una gráfica con los siguientes datos
dates = ['2022-25-10', '2022-26-10', '2022-27-10']
temperatures = [10, 11, 15]
#cambio la escala en y con el slider
temperatures = [days*i for i in temperatures]

figure = px.line(x=dates, y=temperatures, labels={'x':'Date', 'y':'Temperature (C)'})
st.plotly_chart(figure)