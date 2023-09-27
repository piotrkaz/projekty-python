import requests
import json

table = 'a'
date = '2023-09-27'
url = f'http://api.nbp.pl/api/exchangerates/tables/{table}/{date}/?format=json'
print(url)
response = requests.get(url)
data = response.json()
print(data)

temp_file = json.dumps(data)
with open('dump_file.json', 'w') as file:
    file.write(temp_file)