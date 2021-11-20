'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Formatacao_Dados.py
Infelizmente nem sempre os dados chegam prontos para o trabalho, assim
é importante saber formatá-los para o devido uso. Abaixo segue alguns exercícios 
que fiz para formatação de dados.
'''

# Rotina
empresa = 'Google'
print(empresa)

empresa = "Google"
print(empresa)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])

empresa = "Let's Go"
print(empresa)

frase = "O professor Gabriel da Let's Go disse: \"Hoje a pizza é por minha conta\""
print(frase)

nomes_cidades = "São Paulo, Belo Horizonte, Rio de Janeiro, Brasília"
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)

cabecalho = '                              Menu Principal                    '
print(cabecalho.strip())

nome_cidade = 'rIo DE jaNeirO'
print(nome_cidade.title())
print(nome_cidade.capitalize())
print(nome_cidade.lower())
print(nome_cidade.upper())

nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('Tenta de novo, vai')
    nome_cidade = input('Que cidade do Brasil é conhecida como cidade maravilhosa?')

print('Muito Bem!')

mensagem = 'Você viu o que o Gabriel disse na sala ontem?'
fui_citado = 'Gabriel' in mensagem
print(fui_citado)
