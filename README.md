# DASHBOARD DE PRONÓSTICO DEL TIEMPO EN EL MUNDO

El presente proyecto se lo a realizado en streamlit. El mismo muestra la temperatura de 1 a 5 días y de igual forma muestra el pronóstico del clima de 1 a 5 días con imágenes y fecha.

El programa consta de dos scripts, uno denominado main.py, que muestra los datos en un dashboard mediante la aplicación web streamlit.

Los datos son extraidos a través del script backend.py. En el mismo se a construido una API, para traer los datos desde: https://api.openweathermap.org/

Para mostrar los datos, se escribe el lugar y se selecciona la variable a visualizar, que en este caso es temperatura. De igual forma se mueve el slider del número de días y se obtiene la siguiente gráfica:

![temperatura](https://github.com/krist2357/app7/assets/75154211/08205ec4-9e31-4e51-b5a4-78a06a90c8fd)

Para el caso de revisar el clima, se selecciona clima y se obtiene para un día:

![clima](https://github.com/krist2357/app7/assets/75154211/e6109582-83a5-400f-a898-2d8f274451ba)
