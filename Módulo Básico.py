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

# cidade = input('Que cidade do Brasil é conhecida como "cidade maravilhosa"? ')
# cidade = cidade.strip()
# while cidade.lower() != 'rio de janeiro':
#     print('Tende novamente')
#     cidade = input('Que cidade do Brasil é conhecida como "cidade maravilhosa"? ')

print('Certo!')

print('Formatar escrita das strings')

nome = 'Felipe'
anos = 35
filhos = 2
print(f'{nome} tem {anos} anos e {filhos} filhos')  # Exemplo de texto.
print('{} tem {} anos e {} filhos'.format(nome, anos, filhos))  # Outro tipo

gasolina = 3.4765
print('O preço da gasolina subiu e está em R$ {:.2f}'.format(gasolina))  # formatar os 0 na virgula
print()


print('Dicionário: Se armazena dentro de {}')  # Relaciona uma série de valores como se fosse uma lista, só que melhor

cidade = {  # Estrutura mais flexivel
    'nome': 'São paulo',
    'estado': 'São paulo',
    'area': 1521,
    'populacao': 12.18,
}
print(type(cidade))
print(cidade)

cidade['Pais'] = 'Brasil'  # Só isso já add ao final do dicionário
print(f'Adicionando ao final do Dic:', cidade)

cidade['area'] = 1500  # Altera o valor especificado.
print(f'Altera um valor que vc pode especificar:', cidade)

# ELE ALTERA O VALOR DO DICIONÁRIO ORIGINAL!!!

cidade2 = cidade
cidade2['nome'] = 'Santos'
print(f'Novo Dic:', cidade2)
print(f' Também altera o original:', cidade)
# O dic 1 e 2 agora tem o mesmo nome de cidade. Para mudar somente 1 dos Dics usar .copy()

cidade3 = cidade.copy()
cidade3['estado'] = 'Rio de Janeiro'
print(f'Função .copy() permite fazer novo Dic e n altera valor do Dic original:', cidade3)
print(f'Cidade original:', cidade)
print(f'Alteração com .copy():', cidade3)
print()


novos_dados = {  # Posso adicionar um conjunto de novas informações
    'populacao': 15.00,
    'nome': 'São Paulo',
    'fundacao': '25/01/1554'
    }
cidade.update(novos_dados)  # Dar update no novo Dic antes de chamar eles
print(cidade)

# Quando eu n tenho ctz de qual dado tem dentro do meu dic eu posso usa .get para procurar sem dar erro:

print(cidade.get('prefeito'))
# Procurando prefeito dentro de cidade e retorna valor "None" pq não tem isso especificado.

print()
print('Outras modificações: ')

print(cidade.keys())  # Retorna uma lista com as chaves do Dic
print(cidade.values())  # Retorna uma lista com os valores das chaves do Dic
print(cidade.items())  # Retorna uma lista de tuplas com a chave e o valor junto

