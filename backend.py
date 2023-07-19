import requests
API_KEY = "xxxxxxxxxxxxxxx" # API KEY a configurar en la página https://api.openweathermap.org/

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place},ec&APPID={API_KEY}"
    #Realizar la solicitud de la URL
    response = requests.get(url)
    #El contenido será traido como JSON.
    data = response.json()
    #Para construir la siguiente línea, se realizó un debug.
    #En el mismo se visualiza una variable List. La cual es una lista que contiene un diccionario.
    filtered_data = data['list']
    #Si se observa la longitud de los datos filtrados, los mismos dan 40. 
    #Esto quiere decir que en 5 dias se han realizado
    #8 observaciones en un día
    nr_values = 8*forecast_days # 8 observaciones
    filtered_data = filtered_data[:nr_values] 
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Quito",forecast_days=3)) #Mostrar en consola la data de quito en 3 días.
