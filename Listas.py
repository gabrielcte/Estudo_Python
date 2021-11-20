nomes_cidades = ['São Paulo', 'Londres', 'Toquio', 'Paris']
for nome in nomes_cidades:
    print(nome)

contador = 0
while contador < len(nomes_cidades):
    print(nomes_cidades[contador])
    contador = contador + 1

nomes_cidades = 'São Paulo', 'Londres', 'Toquio', 'Paris'
for nome in nomes_cidades:
    print(nome)

cidade ={
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes': 12.2
}
for nome in cidade:
    nome = 'Rio de Janeiro'
print(nomes_cidades)
nomes_cidades = ['São Paulo', 'Londres', 'Toquio', 'Paris']
for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Rio de Janeiro'
print(nomes_cidades)

print(list(range(10)))
print(list(range(2,10)))
print(list(range(2,10,2)))

fib = [1, 1, 2, 3, 5, 8, 13]
for elemento in fib:
    print(elemento)
# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será 1.

for numero in range(10):
    print(numero)
    # este exemplo imprime os números de 0 a 9, de um em um

# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.

for numero in range(1,11):
    print(numero)
    # este exemplo imprime os números de 1 a 10, de um em um

# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1,20,2):
    print(numero)
    # este exemplo imprime os ímpares positivos menores do que 20
    # ele começa valendo 1 e salta de 2 em 2 até atingir ou passar 20

# O incremento pode ser também um decremento (incremento negativo).
for numero in range (10,0,-1):
    print(numero)
    #Imprimindo os números de 1 a 10 em ordem decrescente
