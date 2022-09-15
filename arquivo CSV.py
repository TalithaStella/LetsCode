import csv

print('Arquivo completo')
with open('Documentos/brasil_covid.csv..csv', 'r') as arquivoCSV:  # Abriu o arquivo CSV completamente
    leitor = csv.reader(arquivoCSV)
    for linha in leitor:
        print(linha)

print()

print('Filtro:')
with open('Documentos/brasil_covid.csv..csv', 'r') as arquivoCSV:
    leitor = csv.reader(arquivoCSV)
    header = next(leitor)  # Pra n mostrar o header colocar 'next'
    for linha in leitor:
        if float(linha[2]) > 1:  # Vai mostrar somente os dados que tiver casos novos [2] > 1
            print(linha)  # Basicamente filtrou o documento

print()

print('Da pra abrir o documento sem ter a biblioteca (??).')
with open('Documentos/brasil_covid.csv..csv', 'r') as fileCSV:
    linhas = fileCSV.read()  # Ler todas as linhas do arquivo
    linhas = linhas.split('\n')  # Separar em lista (\n é quebra de linha)
    for linha in linhas:  # Pra cada linha em conjunto de linhas
        linha = linha.split(',')  # Separou pela ',' que é o que separa os dados
        print(linha)


# Pelo que entendi dessa maneira n precisa da primeira parte 'import csv'

print()

print('Escrevendo em arquivo CSV')

with open('Documentos/user.csv', 'w', newline='') as userCSV:
    escritor = csv.writer(userCSV)
    escritor.writerow(['Nome', 'Sobrenome', 'E-mail', 'Gênero'])
    escritor.writerow(['Talitha', 'Oliveira', 'huidsha@gmail.com', 'Fem'])

print()


print('Questionario:')

# Variáveis de cabeçalho e entrada de dados
header = ['Nome', 'Sobrenome:']
dados = []

# Aqui o \n da a quebra de linha e coloca 1 pergunta em cada linha
opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')

while opt != '0':  # Se a resposta não for 0 ele continua (pode ser literalmente qq coisa, n necessáriamente o n 1):
    nome = input('Primeiro nome: ')
    sobrenome = input('Sobrenome: ')
    dados.append([nome, sobrenome])  # append pra adicionar esses valores na variável 'dados'
    opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')  # add novamente a pergunta pra voltar o loop ou sair

print(f'Só mostrando os dados: ', dados)
print()

# Primeiro abre o documento de escrita:
with open('Documentos/cadastro.csv', 'w', newline='') as cadastroCSV:
    writer = csv.writer(cadastroCSV)  # Escritor - chamar método writer
    writer.writerow(header)  # Chama a variável reader que definimos lá em cima
    writer.writerows(dados)  # E os dados que foram adicionados no laço While


# Depois abre o documento só pra ler:
with open('Documentos/cadastro.csv', 'r') as cadastro_leitorCSV:  # as outronome
    csv_reader = csv.reader(cadastro_leitorCSV, delimiter=',')  # Chama como reader
    for linha in cadastro_leitorCSV:  # Para cada 'row' no leitor, mostrar o row:
        print(linha)




