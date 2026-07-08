import requests
import json

api_response = requests.get('https://api.open-meteo.com/v1/forecast?latitude=17.3850&longitude=78.4867&current=temperature_2m,relative_humidity_2m,wind_speed_10m')

weather = json.loads(api_response.text)

print (f"""Temperature : {weather["current"]["temperature_2m"]}{weather["current_units"]["temperature_2m"]} 
Humidity : {weather["current"]["relative_humidity_2m"]}{weather["current_units"]["relative_humidity_2m"]} 
Wind Speed : {weather["current"]["wind_speed_10m"]}{weather["current_units"]["wind_speed_10m"]} 
""")