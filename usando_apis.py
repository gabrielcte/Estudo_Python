import requests
url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
print(req.status_code)

dados = req.json()
print(dados)

valor_reais = float(input('Informa o valor em R$ a ser convertido\n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dolar valem US$ {(valor_reais/cotacao):.2f}')
