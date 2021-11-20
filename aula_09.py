empresa = 'Google'
print(empresa)

empresa = "Google"
print(empresa)

empresa = "Let's Code"
print(empresa)

frase = "O professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])


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

print('Boooa, campeão!')

mensagem = 'Você viu o que o Pietro disse na sala ontem?'
fui_citado = 'Pietro' in mensagem
print(fui_citado)