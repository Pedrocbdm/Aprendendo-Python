def entidade(a):
    if a == "me ajude calculadora2000":
        while a != 'me ajude Calculadora2000': #nota de aprendizado: no uso de 'while', não é correto, em maior parte dos casos, adicionar um 'return' na sua indentação, nesse caso, logo abaixo da input, pois isso vai encerrar a cadeia do 'while'. Então, a posição correta do 'return' é na mesma indentação do 'while', assim, o return só irá fornecer um valor após a condição do 'while' ser cumprida. 
            a = input("Como ousa me desrespeitar??? Calculadora2000, com C maiúsculo. Tente pedir ajuda de novo, direitinho: ")
            if a == 'Calculadora2000':
                while a != 'me ajude Calculadora2000':
                    a = input('PEÇA AJUDA, *me ajude Calculadora2000*: ')
                return a 
        return a 
    elif a == 'me ajude Calculadora2000': #input correta
        print('Certo, irei conceder meu conhecimento a você')
        return ' '
    elif a == 'me ajude Calculadora 2000': #caso o usuário escreva Calculadora2000 separado
        while a != 'me ajude Calculadora2000':
           a = input('Calculadora2000, tudo junto, voce não entende? Peça ajuda de novo: ')
           if a == 'Calculadora2000':
                while a != 'me ajude Calculadora2000':
                    a = input('PEÇA AJUDA, *me ajude Calculadora2000*: ')
                return a 
        return a
    elif a == 'me ajude calculadora 2000': #caso o usuário escreva com c maiúsculo e separado
        while a != 'me ajude Calculadora2000':
           a = input('C maiúsculo, Calculadora2000, tudo junto, voce está testando minha paciência. Vamos lá, tente pedir ajuda mais uma vez: ')
           if a == 'Calculadora2000':
                while a != 'me ajude Calculadora2000':
                    a = input('PEÇA AJUDA, *me ajude Calculadora2000*: ')
                return a 
        return a
    elif a == 'Me ajude Calculadora2000':
        while a != 'me ajude Calculadora2000':
            a = input('Não consegue ver a entidade que está na sua frente!? Você realmente acha que estamos em pé de igualdade para você escrever *Me ajude* com m maiúsculo??? Eu sou o ser superior aqui, só o meu nome deve começar com letras maiúsculas: ')
        return a 
    elif a != 'me ajude Calculadora2000':
        while a != 'me ajude Calculadora2000':
            a = input('Como você espera que eu entenda o que está falando enquanto você digita errado? Olha, vou te ajudar, escreva *me ajude Calculadora2000*, sem os asteríscos: ')
            if a == '*me ajude Calculadora2000*':
                while a != 'me ajude Calculadora2000':
                    a = input('Sua incapacidade de seguir comandos básicos me entristece, é realmente deprimente. Não vou me estressar com isso. Só escreve *me ajude Calculadora2000*, sem os asteríscos: ')
        return a
        
clamar = input("se ajoelhe e clame pela a ajuda da Calculadora2000 *me ajude Calculadora2000*: ") #input que define a variável que vai ser usada na fórmula 

print(entidade(clamar)) #esse comando vai printar o resultado da formula "entidade" de acordo com a input realizada no comando acima
        
def duvidas(d):
    if d == 's':
        d = input('Qual você deseja aprender sobre? Raiz ou potencia?: ').lower()
        if d == 'raiz':
            print('Certo, o primeiro valor que você deve inserir é a base, o número que estiver dentro da raiz, o segundo valor deve ser o indice da raiz, simples assim.')
            d = ' '
            return d
        if d == 'potencia':
            print('Ok, o primeiro valor que você deve inserir é a base, o segundo valor deve ser a potência, simples assim.')
            d = ' '
            return d
    if d == 'n':
        d = ' '
        print('Certo, então continuemos para o que realmente importa.')
        return d 

duvida = input('Antes de tudo, você deseja saber como realizar os cálculos de raiz e potência? *s/n*: ')

print(duvidas(duvida))

def calculadora(n1,op,n2):
    if op == "somar":
        return n1+n2 
    elif op == "subtrair":
        return n1-n2
    elif op == "multiplicar":
        return n1*n2
    elif op == 'dividir':
        return n1/n2
    elif op == 'potencia': 
        x = n1
        while n2 > 1:
            x = (x * n1)
            n2 = n2 - 1
        return x
    elif op == 'raiz':
        return n1 ** (1/n2)
        
numero1 = int(input("digite um valor: "))
operacao = input("o que deseja fazer? Somar, dividir, multiplicar, subtrair, potencia, raiz?: ").lower() #o ".lower()" é responsável por transcrever a input do usuário para letras minúsculas
numero2 = int(input("digite o segundo valor: "))

print(calculadora(numero1,operacao,numero2))
print('Não precisa agradecer a Grande Calculadora2000, ela não tem tempo para ouvir isso.')
