"""
Tipo uma função, mas que n ta no seu projeto de fato, e que vem de algum lugar externo.

Ex: Site de fofoca: Conteúdo fofoca, mas pode ter informações sobre o clima, e isso, como n faz parte do projeto
principal (clima) pode vir de uma API.

Pode ser para criar algo novo, ou para alteração

Sempre que for usar uma API olhar a documentação.


"""

"""!pip install requests

url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)  # Tem outros modos além de .get

print(req.status_code)  # Se aparecer 200 é pq ta tudo certo GGWP

200
dados
dados = req.json()

print(dados)

valor = float(input('Valor em R$ a ser convertido: '))
cotacao = dados['rates']['BRL']
print(f' R$ {valor} em dolar valem {(valor / cotacao):.2f}')
Valor em R$ a ser convertido: 200
 R$ 200.0 em dolar valem 38.56
 
 
 """





