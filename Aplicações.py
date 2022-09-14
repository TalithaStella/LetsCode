"""
Manipulação de arquivos - Tentando aqui no pycharm, mas se pa só funciona no jupyter

"""

# Abrir arquivo de local anterior ao que eu estou trabalhando, add: ../ quantas pastas precisar 'subir' (acima)
# Abrir arquivo dentro de alguma pasta dentro da pasta que estou trabalhando, add: nomedapasta/nomedoarquivo (abaixo)

# variável = open('nomedoarquivo), modo de abertura (lendo ou escrevendo?)
print('abrindo arquivo em modo "ler".')
print()

arquivo = open('leitura.txt', 'r')  # Para ler coloque 'r'

texto = arquivo.read()
print(texto)  # Uaaaaau
arquivo.close()
# SEMPRE TEM QUE FECHAR O ARQUIVO

print()
print('__________________________')
print()

# Caso eu precise analisar linha a linha do meu arquivo:

print('>>>>>>> Abrindo o arquivo usando While:')
print()

arquivo = open('leitura.txt', 'r')
linha = arquivo.readline()
# Leitura de arquivo faz um 'cursor' entao se ele lê uma linha ele n volta pra onde ele estava, só segue em frente
while linha != '':  # Enquanto linha dor diferente de valor vazio
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()

print()
print('__________________________')
print()

print('>>>>>> Abrindo o arquivo usando For:')
print()

arquivo = open('leitura.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()


print()
print('__________________________')
print()


print('>>>>>> O python sabe que a gente tem que fechar o arquivo, entao escreva assim:')
print()

with open('leitura.txt', 'r') as arquivo:
    texto = arquivo.read()
    print(texto)

print()
print('__________________________')
print()

print('>>>>>> Modo escrever em arquivo: ')
print()

with open('escrita.txt', 'w') as arquivo:  # Trocou o r por w
# ELE SOBREESCREVE TODO SEU ARQUIVO ORIGINAL - CUIDADO PRA N PERDER SEU ARQUIVO MÃE
    arquivo.write('LINHA QUE ADD USANDO PYTHON\n')
    arquivo.write('SEGUNDA LINHA QUE ADD USANDO PYTHON\n')

with open('escrita.txt', 'r') as arquivo:
    print(arquivo.read(), end='')

print()
print('>>>>>> Modo adicionar informação em arquivo: ')  # Trocou w por a
print()

with open('escrita.txt', 'a') as arquivo:  # Modo de abertura 'a'
    arquivo.write('TERCEIRA LINHA QUE ADD USANDO PYTHON\n')  # Esse n apaga tudo

with open('escrita.txt', 'r') as arquivo:
    print(arquivo.read(), end='')


print()
print('>>>>>> Modo adicionar misto ')  # Trocou r+
print()

# Claramente n deu certo kkkk  - mas n sei o que aconteceu, pq erro n deu.
with open('escrita.txt', 'r+') as arquivo:
    arquivo.write('TESTANDO R+ KKK \n')
    print(arquivo.read(), end='')






