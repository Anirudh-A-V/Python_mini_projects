import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"
city = input("Enter the city name and country code : ")

query = {"q": city, "units": "metric"}

headers = {
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": "e228ed9bcdmsha1fc0c3f1222c75p1d3eafjsn15f97a40c083"
}

response = requests.request('GET', url, params=query, headers=headers)

print(f"\nCity name : {response.json()['name']}")
print(f"City coordinates : {response.json()['coord']}\n")
print(f"Weather Conditions : {response.json()['weather'][0]['main']}, {response.json()['weather'][0]['description']}")
print(f"Temperature : {response.json()['main']['temp']}, min - {response.json()['main']['temp_min']}, max - {response.json()['main']['temp_max']}")
print(f"Pressure : {response.json()['main']['pressure']} hPa")
print(f"Humidity : {response.json()['main']['humidity']} %")
print(f"Visibility : {response.json()['visibility']} m")
print(f"Wind : {response.json()['wind']['speed']} km/hr, {response.json()['wind']['deg']} degrees\n")
