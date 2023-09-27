import requests
import json

table = 'a'
date = '2023-09-27'
url = f'http://api.nbp.pl/api/exchangerates/tables/{table}/{date}/?format=json'
response = requests.get(url)
data = response.json()

temp_file = json.dumps(data)
with open('dump_file.json', 'w') as file:
    file.write(temp_file)
print('Zrzucono dane do pliku.')

temp = json.dumps(data, indent = 3)
#print(temp)

temp2 = json.dumps(data[0].)
print(temp2)