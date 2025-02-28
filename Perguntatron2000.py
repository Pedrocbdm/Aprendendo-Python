perguntas = []
incertezas = []

p = input('Bem vindo! Qual a primeira pergunta que deseja registrar?: ')
perguntas.append(p)

continuar = input('Você tem mais perguntas? s/n: ')
while continuar == 's':
    p = input('Certo, qual a sua próxima pergunta?: ')
    perguntas.append(p)
    continuar = input('Você tem mais perguntas? s/n: ')

while perguntas != []:
    print(' ')
    import random
    pergunta_aleatória = random.choice(perguntas)
    x = pergunta_aleatória
    input('{} Qual sua resposta?: '.format(x))
    d = input('Você têm certeza da sua resposta? s/n: ')
    if d == 'n':
        incertezas.append(x)
    perguntas.remove(x)

print(' ')
print('Essas são as perguntas que você têm dúvida: {}'.format(incertezas))