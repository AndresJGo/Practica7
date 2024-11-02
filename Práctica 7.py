import requests
import json

user = "ajimenezg1801"
base_url = "http://api.geonames.org/postalCodeSearchJSON?postalcode=53800&maxRows=10&username=" + user
lat = 0
lng = 0

response = requests.get(base_url)
JSON = response.content.decode('utf-8')
data = json.loads(JSON)

for dir in data["postalCodes"]:
    if dir["countryCode"] == "MX":
        print(dir)
        lat = dir["lat"]
        lng = dir["lng"]
        break

print("\nLatitud encontrada: ",lat, "Longitud Encontrada: ", lng)

APIKEY = "ce675568aae230e6a9df2e191bc43ed3"

URLweather = "http://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) +"&lon=" + str(lng) + "&appid=" + APIKEY
finalResponse = requests.get(URLweather)
finalJSON = finalResponse.content.decode('utf-8')
finalData = json.loads(finalJSON)

print("Información del clima en esas coordenadas:\n",finalData["weather"][0]["main"], finalData["weather"][0]["description"])

