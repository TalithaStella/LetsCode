""" Lista: definido por valores em [], pode ser alterado (olhar Aula 18 - Listas em Python)


Tuplas contempla alterações diferentes da lista. Considerada mais "rigida"
Contém capacidade menor de armazenamento

tupla = ('ex', 'ex2', 'ex3', 'ex4')
tupla2 = 'ex', 'ex2', 'ex3', 'ex4'  - sem ()

O importante pra tupla é colocar a virgula.

tupla_1_elemento = 'ex1',
"""

tupla1 = ('ex', 'ex2', 'ex3', 'ex4')
print(tupla1)

tupla2 = 'ex', 'ex2', 'ex3', 'ex4'
print(tupla2, type(tupla2))

tupla_1elemento = 'ex1',
print(tupla_1elemento, type(tupla_1elemento))

# Funções aceitas na tupla: len, indexação (?) [:] e fatiamento.

# Função só da tupla: unpacking
print()
paises = 'Brasil', 'Canadá', 'Japão', 'China', 'Argentina'

b, c, j, ch, a = paises
print('função unpacking: ', b, c, j)
print(*paises)  # Desenpacotou


print('______________')
print('Mais possibilidades com Strings:')

# Para ignorar um caracter, usar contra barra \
frase = ("O prof da Let's Code disse \"Hoje a pizza é por minha conta\"")
print(frase)
print()

print('Função split: Separa os elementos')
paises1 = "Brasil, Canadá, Japão, China, Argentina"
paises1 = paises1.split(', ')  # ele entendeu que o que separa os conteúdos das strings é p ", "
print(paises1)
print()

print('"Limpar espaços ou dados indesejados: strip')
cabecalho = '                   MENU                          '
print(cabecalho.strip())  # Se tentar selecionar n vai aparecer os espaços
print()

print('Formatação de texto: title, capitalize, lower, upper')
formatacao = 'SaO pAuLo'

print(formatacao)
print(formatacao.title())  # Primeiras palavras com letra maiúscula
print(formatacao.capitalize())  # Primeira letra da 1ª palavra com letra maiúscula
print(formatacao.lower())  # tudo pequeno
print(formatacao.upper())  # tudo grande
print()

""" O uso de strip junto com as formatações de texto podem ser usadas na hora de receber dados,
assim o interpretador não vai se confundir com espaços e ou letra que pode ter escrito maiusculo ou minusculo

Ex:"""

cidade = input('Que cidade do Brasil é conhecida como "cidade maravilhosa"? ')
cidade = cidade.strip()
while cidade.lower() != 'rio de janeiro':
    print('Tende novamente')
    cidade = input('Que cidade do Brasil é conhecida como "cidade maravilhosa"? ')

print('Certo!')




