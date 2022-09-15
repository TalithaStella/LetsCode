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

print(*final_data, sep='\n')

