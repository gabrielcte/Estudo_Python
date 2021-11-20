'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Funcao_e_args.py
Quando temos atividades repetídas é aconselhado fazer funções e chamá-las durante o
código.
'''

# Definindo funções

def hello():
    print('Olá, mundo!')


def calcula_media(*args, margem=0):
    soma = sum(args)
    media = soma / len(args)
    return media + margem


def print_info(**kwargs):
    print(kwargs, type(kwargs))


def calcula_media_3_numeros(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

# Rotina
resultado = calcula_media_3_numeros(9, 10, 8)
print(resultado)

resultado2 = calcula_media_3_numeros(valor1=9, valor2=10, valor3=5)
print(resultado2)

print('Olá', end=' ')
print('Pietro')

resultado = calcula_media(9)
print(resultado)

print(calcula_media(10, 8, 9, 4, 3, margem=0.3))
print(print_info(nome='Gabriel', sobrenome='Silva'))
