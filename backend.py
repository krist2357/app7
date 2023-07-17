import requests
API_KEY = "5d8990e912117488270a09e634383792"

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place},ec&APPID={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    #Aqui, si se ve la longitud de los datos filtrados. Dan 40. esto quiere decir que en 5 dias se han realizado
    #8 observaciones en un día
    nr_values = 8*forecast_days # 8 observaciones
    filtered_data = filtered_data[:nr_values] 
    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Quito",forecast_days=3))