
import requests

from config.config import Weather_API_KEY

# Global Variables
city = "Ankara"
country_code = 'TR'

startdate = 1606435200
enddate = 1704067140

#End Global Variables


#Functions
def get_lat_log(city:str,country_code:str):

   city_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country_code}&limit=5&appid={Weather_API_KEY}"
   city_url = city_url.replace(" ", "%20")
   
   responce = requests.get(city_url).json()

   lat = responce[0]['lat']
   long = responce[0]['lon']

   return lat,long


def request_init(lat,long,start,end):

    current_air_pollution = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={long}&appid={Weather_API_KEY}"
    forecast_air_pollution = f"http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={lat}&lon={long}&appid={Weather_API_KEY}"
    historical_air_pollution = f"http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={long}&start={start}&end={end}&appid={Weather_API_KEY}"

    current_air_pollution = current_air_pollution.replace(" ", "%20")
    forecast_air_pollution = forecast_air_pollution.replace(" ", "%20")
    historical_air_pollution = historical_air_pollution.replace(" ", "%20")

    current_response = requests.get(current_air_pollution).json()
    forecast_response = requests.get(forecast_air_pollution).json()
    historical_response = requests.get(historical_air_pollution).json()

    return current_response,forecast_response,historical_response

def get_request():

    lat,long = get_lat_log(city, country_code)

    return  request_init(lat,long,startdate,enddate)


"""if __name__ == '__pandas_init__':
    get_request()"""