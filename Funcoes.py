def hello():
    print('Olá, mundo!')

def calcula_media(valor1=0, valor2=0, valor3=0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(9,10,8)
print(resultado)

resultado2 = calcula_media(valor1=9,valor2=10,valor3=5)
print(resultado2)

print('Olá', end=' ')
print('Pietro')

resultado = calcula_media(9)
print(resultado)
