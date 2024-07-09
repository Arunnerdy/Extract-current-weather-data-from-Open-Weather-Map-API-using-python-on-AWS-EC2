import json
from datetime import datetime
import pandas as pd 
import requests

lat = "12.914142"
lon = "74.855957"
base_url1 = "https://api.openweathermap.org/data/2.5/weather?lat="
base_url2 = "&lon="

with open("credentials.txt","r") as f:  #create a text file name credentials where paste your API key from openweather
    api_key = f.read()
final_url = base_url1+lat+base_url2+lon+"&appid="+api_key

def kelvin_to_fahrenheit(temp_in_kelvin):
    temp_in_fahrenheit = (temp_in_kelvin - 273.15) * (9/5) + 32
    return temp_in_fahrenheit
def etl_weather(url):
    r = requests.get(url)
    data = r.json()
    #print(data)

    city = data["name"]
    weather_description = data["weather"][0]['description']
    temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp"])
    feels_like_farenheit= kelvin_to_fahrenheit(data["main"]["feels_like"])
    min_temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp_min"])
    max_temp_farenheit = kelvin_to_fahrenheit(data["main"]["temp_max"])
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    time_of_record = datetime.fromtimestamp(data['dt'] + data['timezone'])
    sunrise_time = datetime.fromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_time = datetime.fromtimestamp(data['sys']['sunset'] + data['timezone'])


    transformed_data = {"City": city,
                        "Description": weather_description,
                        "Temperature (F)": temp_farenheit,
                        "Feels Like (F)": feels_like_farenheit,
                        "Minimun Temp (F)":min_temp_farenheit,
                        "Maximum Temp (F)": max_temp_farenheit,
                        "Pressure": pressure,
                        "Humidty": humidity,
                        "Wind Speed": wind_speed,
                        "Time of Record": time_of_record,
                        "Sunrise (Local Time)":sunrise_time,
                        "Sunset (Local Time)": sunset_time                        
                        }
    transformed_data_list = [transformed_data] #convert the data to list
    df_data = pd.DataFrame(transformed_data_list)# make a data frame
    #print(df_data)

    df_data.to_csv("current_weather_data_mangalore.csv", index = False)

if __name__ =="__main__":
    etl_weather(final_url)

