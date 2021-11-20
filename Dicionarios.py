'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Dicionarios.py
Aqui são os exercícios que fiz para aprender o uso de dicionários no Python.
'''

# Rotina
dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.33,
}
print(type(dados_cidade))
print(dados_cidade)

dados_cidade['pais'] = 'Brasil'
print(dados_cidade)
print(dados_cidade['nome'])

dados_cidade['area_km2'] = 1500
print(dados_cidade)

dados_cidade_2 = dados_cidade
dados_cidade_2['nome'] = 'Santos'
print(dados_cidade)
print(dados_cidade_2)

dados_cidade_3 = dados_cidade.copy()
dados_cidade_3['estado'] = 'Rio de Janeiro'
print(dados_cidade)
print(dados_cidade_3)

novos_dados = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}
dados_cidade.update(novos_dados)
print(dados_cidade)
print(dados_cidade.get('prefeito'))
print(dados_cidade.keys())
print('----')
print(dados_cidade.values())
print('----')
print(dados_cidade.items())

# O dicionário é definido pelos símbolos { e }

dicionario = {}

# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))

# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)

# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' in dicionario:
    print('cat existe!') 
if 'bird' in dicionario:
    print('bird existe!')
if 'gato' in dicionario:
    print('gato existe!')

'''
Também podemos utilizar as funções .keys() e .values() para obter listas
com apenas as chaves ou apenas os valores do dicionário.
'''
chaves = dicionario.keys()
print(chaves)

valores = dicionario.values()
print(valores)

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário
itens = dicionario.items()
print(itens)
