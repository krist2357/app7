# DASHBOARD DE PRONÓSTICO DEL TIEMPO EN EL MUNDO

El presente proyecto se lo a realizado en streamlit. El mismo muestra la temperatura de 1 a 5 días y de igual forma muestra el pronóstico del clima de 1 a 5 días con imágenes y fecha.

El programa consta de dos scripts, uno denominado main.py, que muestra los datos en un dashboard mediante la aplicación web streamlit.

Los datos son extraidos a través del script backend.py. En el mismo se a construido una API, para traer los datos desde: https://api.openweathermap.org/

Para mostrar los datos, se escribe el lugar y se selecciona la variable a visualizar, que en este caso es temperatura. De igual forma se mueve el slider del número de días y se obtiene la siguiente gráfica:

![image](https://github.com/krist2357/app7/assets/75154211/cdbd2b98-92c3-4280-929c-94de227ab8bc)

Para el caso de revisar el clima, se selecciona clima y se obtiene para un día:

![image](https://github.com/krist2357/app7/assets/75154211/fe6b0870-e13f-4e55-b7bc-53f68a600d50)
