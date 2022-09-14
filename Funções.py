"""
Função: Vc cria um sequência de passos para ser seguidos em vários momentos, e ao invés de ficar escrevendo sempre
só 'chama' aquela função para ser executada.

def - nomedafunção(campodereceberdados pode ser vazio):
    print('Hello')

nomedafunção()
"""

def hello():
    # Essa função, quando chamada faz aparecer esse print.
    print('Eai gay')

hello()
# Pra chamar a função é só escrever o nome dela.
print()


def calcular_media(v1, v2, v3):
    media = (v1 + v2 + v3) / 3
    return media

resultado = calcular_media(10, 10, 10)  # Pra que fazer isso aqui??
print(resultado)

print(calcular_media(10, 1, 10))

def media2(*args):
    med = sum(args) / len(args)
    return med

print(media2(10, 8, 9))

def info(**kwargs):  # Retorna um dicionario
    print(kwargs, type(kwargs))

info(nome='Lhok', nome2='Talitha', nome3='Stella')




