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

# print(*final_data, sep='\n')


# DateTime faz str se tornarem datas reais.
import datetime as dt

# natal = dt.date(2020, 12, 25)
# reveillon = dt.date(2021, 1, 1)
# print(reveillon-natal)  # Quanto tempo tem entre essas datas
# print((reveillon-natal).days)
# print((reveillon-natal).seconds)  # N usei o tipo 'time' só o 'date' = n contou o tempo (tb da pra contar microseconds)

import csv

with open('Documentos/projeto_covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
    final_data[i][data] = dt.datetime.strptime(final_data[i][data], '%Y-%m-%d')

# print(*final_data, sep='\n')

# a partir daqui estamos preparando a API que plota os gráficos, então vamos preparar "helpers" que monta os gráficos


# Responsável pela chave data set da API que constrói os dados de Y
def get_datasets(y, labels ):  # dados reais de Y e uma lsita que contem os labels dos dados
# O Y pode ter mais de 1 função então verificar:
    if type(y[0]) == list:  # Se esse Y na posição 0 for uma lista
        datasets = []  # Caso seja uma lista inicia essa variável que é uma lista que contém os valores y e labels
        for i in range(len(y)):  # Vai explorar o y E labels
            datasets.append({  # Adiciona em um dicionário
                'label': labels[i],  # n entendi direito o [i] 'na posição atual
                'data': y[i]  # n entendi direito o [i] 'na posição atual
            })
        return datasets

    else:  # Caso o Y n seja uma lista de listas retorna uma lista com unico valor de dicionário
        return [
            {
            'label': labels[0],  # Lista de labels na posição 0
            'data': y  # e os dados são o próprio y
            }
        ]

# Define o título do gráfico
def set_title(title=''):  # str vazia para caso n tenha título (??)
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {  # Retorna um Dic
        'title': title,
        'display': display  # Diz se vai ser mostrado ou não ->
# Eu só quero mostrar o título caso a váriável título (lá em cima) tenha algum valor.

    }

# Função que cria Dic e representa o gráfico

def create_chart(x, y, labels, kind='bar', title=''):

    datasets = get_datasets(y, labels)  # Recebe o get_dataset e precisa do y e labels
    options = set_title(title)  # Chave responsável pela definição do título e umas outras coisas (coisa da api (?))

    chart = {  # Dicionário que representa o gráfico
        'type': kind,
        'data': {  # Essa data tb é um dicionário
            'labels': x,
            'datasets': datasets
        },  # N esquecer da vírgula quando fecha o Dic mas continua o outro
        'options': options   # estabelecer as opções - Setup de informações como título e pode ser usado pra def eixos

    }
    return chart  # retorna o que a gente acabou de criar no final da função


# Função que faz a requisição la da API utilizando o Dic

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'  # Esse link ta na documentação
    resp = r.get(f'{url_base}?c={str(chart)}')  # Guarda a requisicão na variável

# Isso vai retornar a imagem em si, o arquivo de img.
# Pra poder utilizar/armazegar é necessário uma função com o 'content' da requisição. Nesse caso é um valor binário
    return resp.content  # Aqui seria o Json, mas nesse caso como é binário tem que ser .content

# Função responsável por salvar a imagem

def save_image(path, content):
    with open(path, 'wb') as image:  # Aqui é wb pq é a escrita de um valor binário
        image.write(content)


# Além de salvar preciso de uma função pra mostrar a imagem
# importando biblioteca

from PIL import Image
from IPython.display import display

# Depois de importar as bibliotecas criar função que usa elas

def display_image(path):
    img_pil = Image.open(path)  # Função open desse módulo
    display(img_pil)

# Fim dos helpers.
# Agora criar os dados e gerar gráficos

# Plot de barras em grupos mostrando a evolução de confirmados/recuperados
# 2 dados != para y -> recuperados e confirmados

y_data_1 = []
# Vamos utilizar dados pulando de 10 em 10 (meses?)
for obs in final_data[1::10]:
    y_data_1.append(obs[confirm])  # Chama as variáveis lá do conjunto de linhas [29/33]

y_data_2 = []
# Vamos utilizar dados pulando de 10 em 10 (meses?)
for obs in final_data[1::10]:
    y_data_2.append(obs[recup])  # Chama as variáveis lá do conjunto de linhas [29/33]

labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:  # Chama as variáveis lá do conjunto de linhas [29/33]
    x.append(obs[data].strftime('%d/%m/%Y'))  # strftime - Tipo tempo entao transformar devolta para STR

# strptime = str para data
# strftime = data para str

print('Imagem: ')
chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados/Recuperados')
chart_content = get_api_chart(chart)
save_image('Documentos/Primeiro-gráfico.png', chart_content)
display_image('Documentos/Primeiro-gráfico.png')

# A imagem n aparece aqui no Pycharm por motivos que desconheço (AMORZINHO ME SALVAAA), mas funciona o jupyter.

print('QRcode: ')

# Também da pra fazer um QRcode para o gráfico que fizemos.

# Função do QRcode:





from urllib.parse import quote
# from six.moves.urllib.parse import quote





def get_api_qrcode(link):  # Pra onde vai ser redirecionado quando alguém pesquisar

# Pra URL não ficar complexa é importante fazer um 'parse' do nosso valor textual para um valor textual especial de URL
# Pra isso tem que usar uma outra lib = url lib
    text = quote(link)  # parsing do link para url
    url_base = 'htpps://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content  # Binário


# Eu preciso do link responsável por gerar a img do gráfico pra salvar no QRcode
# Então, pra n alterar o cógico, pega a construção lá da linha 118 (get_api_chart)
url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('Documentos/qr-code.png', get_api_qrcode(link))
display_image('Documentos/qr-code.png')







