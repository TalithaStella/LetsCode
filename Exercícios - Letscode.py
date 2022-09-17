"""
Faça um programa que peça ao usuário um número e imprima todos os
números de um até o número que o usuário informar.

 Exemplo:
Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5

"""

# print('Números em ordem decrescente.')
# pergunta = int(input('Digite um número inteiro: '))
# contador = 0
#
# while contador < pergunta:
#     resultado = pergunta - contador
#     contador += 1
#     print(resultado)

# Como coloca as respostas em linha??


print('\n______________________________\n')

"""
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
alguns exemplo abaixo:

Entrada: 25.01 | Saída: (25,50]
Entrada: 25.00 | Saída: [0,25]
Entrada: 100.00 | Saída: (75,100]
Entrada: -25.02 | Saída: Fora de intervalo
"""

valor = float(input('Digite um número: '))

if 0.00 <= valor <= 25.00:
    print(f'Intervalo [0,25]')
elif 25.01 <= valor <= 50.00:
    print(f'Intervalo [25,50]')
elif 50.01 <= valor <= 75.00:
    print(f'Intervalo [50,75]')
elif 75.01 <= valor <= 100.00:
    print(f'Intervalo [75,100]')
else:
    print('Fora de intervalo')



print('\n______________________________\n')

"""
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = pi.r**2.

Dica: Para utilizar um valor mais preciso do pi, você pode importar a biblioteca math, e
utilizar o math.pi, como ilustrado no código abaixo:
"""

pi = 3.14159


def circulo():
    a = pi * raio ** 2
    return a


raio = int(input('Para calcular a área de um círculo informe o valor de raio: '))
print(f'A área do círculo é de {circulo()}')

print('\n______________________________\n')

"""
Questão 4.
Faça um programa que peça 2 números inteiros e um número real,  
calcule e mostre:

a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.

"""

# Número inteiro e número real???

print('Inteiro e reais zzzz')

print('\n______________________________\n')

"""
Vamos fazer um programa para verificar quem é o assassino de um crime. 
Para descobrir o assassino, a polícia faz um pequeno questionário com 5 perguntas 
onde a resposta só pode ser sim ou não:

1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário,
você vai informar como a polícia o considera.
"""

print('Quem é o assassino do crime?\n')

resp = int()

while True:

    perg1 = str(input('Conhece a vítima?\nS ou N? '))
    if perg1 == 's':
        resp += 1

    perg2 = str(input('Já trabalhou com a vítima?\nS ou N? '))
    if perg2 == 's':
        resp += 1

    perg3 = str(input('Telefonou para a vítima?\nS ou N? '))
    if perg3 == 's':
        resp += 1

    perg4 = str(input('Esteve no local do crime?\nS ou N? '))
    if perg4 == 's':
        resp += 1

    perg5 = str(input('Devia para a vítima?\nS ou N? '))
    if perg5 == 's':
        resp += 1

    if resp >= 5:
        print('Vc é o Assassino!')

    elif resp == 4 or resp == 3:
        print('Vc é um Cúmplice.')

    elif resp == 2:
        print('Vc é suspeito.')

    else:
        print('Inocente')

    break
print(f'Sua pontuação foi {resp}! ò-ó')

print('\n______________________________\n')
