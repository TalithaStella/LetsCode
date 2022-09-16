"""
Faça um programa que peça ao usuário um número e imprima todos os
números de um até o número que o usuário informar.

 Exemplo:
Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5

"""


pergunta = int(input('Digite um número inteiro: '))
contador = 0

while contador < pergunta:
    resultado = pergunta - contador
    contador += 1
    print(resultado)

   # Como coloca as respostas em linha??


print('______________________________')


"""
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja
alguns exemplo abaixo:

Entrada: 25.01 | Saída: (25,50]
Entrada: 25.00 | Saída: [0,25]
Entrada: 100.00 | Saída: (75,100]
Entrada: -25.02 | Saída: Fora de intervalo


Q?
"""

print('______________________________')


"""
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da
área desse círculo. Lembrando que a área de círculo é dada pela equação: A = pi.r**2.

Dica: Para utilizar um valor mais preciso do pi, você pode importar a biblioteca math, e
utilizar o math.pi, como ilustrado no código abaixo:
"""






