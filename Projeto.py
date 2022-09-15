"""
Projeto final: Pegar dados sobre COVID-19 de uma API pública e montar alguns dados com ela.

"""

import requests as r  # n sei

url = 'https://api.covid19api.com/dayone/country/brazil'  # Site de onde esta a API
resp = r.get(url)  # 'pega' a api que esta no url (maneira de buscar api??)


# resp.status_code  -- FUNCIONA NO JUPYTER - SE APARECER 200 É PQ DEU CERTO


# guarda os dados retornados pela API
raw_data = resp.json()  # formato de transmissão de dados pela api (maioria)


print(raw_data[0])
print(type(raw_data))


final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['Confirmados', 'Mortos', 'Recuperados', 'Ativos', 'Data'])

confirm = 0
obito = 1
recup = 2
ativo = 3
data = 4

for l in range(1, len(final_data)):  # N entendi nada. pq 1?
    final_data[l][data] = final_data[l][data][:10]

print(*final_data, sep='\n')


# DateTime faz str se tornarem datas reais.
import datetime as dt

natal = dt.date(2020, 12, 25)
reveillon = dt.date(2021, 1, 1)
print(reveillon-natal)  # Quanto tempo tem entre essas datas
print((reveillon-natal).days)
print((reveillon-natal).seconds)  # N usei o tipo 'time' só o 'date' = n contou o tempo (tb da pra contar microseconds)

import csv

with open('Documentos/projeto_covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
    final_data[i][data] = dt.datetime.strptime(final_data[i][data], '%Y-%m-%d')

print(*final_data, sep='\n')







