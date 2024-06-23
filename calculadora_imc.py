print('Bem vindo a Calculadora IMC')

nome = str(input('Qual o seu nome: '))
peso = float(input('Qual o seu peso: '))
altura = float(input('Qual a sua altura: '))

imc = peso / (altura ** 2)


print('Olá {}, o seu peso é {} kgs e sua altura é {} metros'.format(nome, peso, altura))
print('Seu IMC é {:.2f}'.format(imc))

if imc < 18:
    print('Você está abaixo do peso normal')
elif imc < 25:
    print('Você está com sobrepeso')
elif imc < 35:
    print('Você está com obesidade grau I')
else:
    print('Você está com obesidade grau II')