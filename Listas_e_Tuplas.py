nomes_paises = ['Brasil', 'Argetina', 'China', 'Canada', 'Japão']
print(nomes_paises)
print("Tamanho da lista", len(nomes_paises))
print('País', nomes_paises[4])
print('País', nomes_paises[-1])

nomes_paises[4] = 'Colômbia'
print('País', nomes_paises)
print('Paises', nomes_paises[1:3])
print('Paises', nomes_paises[1:-1])
print('Paises', nomes_paises[2:])
print('Paises', nomes_paises[:3])
print('Paises', nomes_paises[:])
print('Paises', nomes_paises[::2])
print('Paises', nomes_paises[::-1])
print(['Brasil'in nomes_paises])
print(['Canada'not in nomes_paises])

lista_capitais = []
lista_capitais.append('Brasília')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')

print(lista_capitais)
lista_capitais.insert(2,'Paris')
print(lista_capitais)
lista_capitais.remove('Buenos Aires')
print(lista_capitais)
removido = lista_capitais.pop(2)
print(lista_capitais,removido)

nomes_paises = ('Brasil', 'Argetina', 'China', 'Canada', 'Japão')
print(nomes_paises)
nomes_paises = 'Brasil', 'Argetina', 'China', 'Canada', 'Japão'
print(nomes_paises,type(nomes_paises))
nome_estado = 'São Paulo',
print(nome_estado,type(nome_estado))
len(nomes_paises)
b, a, c, ca, j = nomes_paises
print(b, c, j)
print(*nomes_paises)
# Criando uma lista vazia.
listavazia = []

# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]

# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]

# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)

# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(numeros[indice])
    indice = indice + 1

indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1

animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta == 's' or resposta == 'S'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)

animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)

jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)

rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)

jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)

digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)

# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)

# Podemos declarar sem parênteses também:
numeros = 1,2,3,5,7,11

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

'''
Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)

# Também pode-se usar o unpacking com uma tupla:
a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)
