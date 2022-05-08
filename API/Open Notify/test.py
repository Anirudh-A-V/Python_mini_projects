import requests, json

response = requests.get('http://api.open-notify.org/iss-now.json?callback=?')

print(response.status_code)

details = json.loads(response.text);
print(details['iss_position']['latitude'])
# details = json.dumps(response.json(), sort_keys=True, indent=4)