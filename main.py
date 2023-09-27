import requests
import json

table = 'a'
date = '2023-09-27'
url = f'http://api.nbp.pl/api/exchangerates/tables/{table}/{date}/?format=json'
print(url)
response = requests.get(url)
response_json = response.json()
print(response_json)

temp_file = json.dumps(response_json)
with open('zrzut.json', 'w') as file:
    file.write(temp_file)