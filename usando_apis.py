'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/usando_apis.py
As APIs são composta por uma série de funções acessíveis somente por programação,
e que permitem utilizar características desse software. Nesse exemplo foi usado uma API publica Web
que tem um conjunto definido de mensagens de requisição e resposta HTTP,expresso no formatos JSON.
'''

# Importando bibliotecas
import requests

# Rotina
url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)

dados = req.json()
print(dados)

valor_reais = float(input('Informa o valor em R$ a ser convertido\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem US$ {(valor_reais/cotacao):.2f}')
