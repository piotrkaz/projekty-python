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

temp2 = json.dumps(data[0]['rates'])

with open('mid_rates.json', 'w') as file:
    file.write(temp2)

print('Zapisano srednie kursy walut.')
print(f'Oto kursy walut z dnia: {date}')

with open('mid_rates.json') as f:
    rates = json.load(f)

for rate in rates:
    print(rate['code'], ' ', rate['mid'])