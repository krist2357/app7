import streamlit as st

st.title('Weather Forecast for the next days')
place = st.text_input('Place: ')
days = st.slider('Forescats Days', min_value=1, max_value=5, help='Select the number the forecast days')
option = st.selectbox('Select data to view',('Temperature','Sky'))
st.subheader(f'{option} for the next {days} days in {place}')
