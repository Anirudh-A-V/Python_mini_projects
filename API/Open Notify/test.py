import requests
import json

response = requests.get('http://api.open-notify.org/astros.json')

# print(response.status_code)

print(f"\nNo. of people in the ISS : {response.json()['number']}")

print(f"List of people in the ISS : ")
for i in response.json()['people']:
    print(i['name'])
