'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Strings_e_Funcao_Print.py
O tipo string tem suas operações e aliada com o print se torna uma forma
importante para os programadores visualizarem o que estão fazendo.
Aqui tem os exercícios de usando string e print.
'''

# Rotina
cumprimento = 'Olá, '
nome = 'Gabriel'
print(cumprimento+nome)
print(nome * 5)

idade = 25
n_filhos = 2
print(nome + ' tem ' + str(idade) + ' anos e ' + str(n_filhos) + ' filhos' )
print('{} tem {} anos e {} filhos'.format(nome,idade,n_filhos))
print(f'{nome} tem {idade} anos e {n_filhos} filhos')

preco_gasolina = 6.237
print('O Preço da gasolina hoje subiu e está em R$ {:.2f}'.format(preco_gasolina))

# Dois operadores aritméticos possuem um comportamento especial em strings:
# Operador de soma (+): concatena (une) 2 strings.
palavra1 = "Bora"
palavra2 = "Codar"
palavra3 = palavra1 + palavra2
print(palavra3)

# Operador de multiplicação (*): copia uma string 'n' vezes:
palavra = 'uma'
trespalavras = 3*palavra
print(trespalavras)

prod = 'chocolate'
preco = 5.14
print('O produto {} custa {}.'.format(prod, preco))

# É possível colocar algumas opções especiais de formatação. Por exemplo:
stringoriginal = 'O litro da gasolina custa {:.2f}'

'''
: indica que passaremos opções
.2 indica apenas 2 casas após o ponto decimal
f indica que é um float
'''

preco = 6.2379265
stringcompleta = stringoriginal.format(preco)
print(stringcompleta)
# O preço sai com apenas 2 casas após a vírgula!

# Pode-se chamar as variávies em diferentes ordens:
print('{2}, {1} and {0}'.format('a', 'b', 'c'))
print('{0}{1}{0}'.format('abra', 'cad'))


# Podemos especificar um número de dígitos obrigatório por campo.
# Vejamos o exemplo:
dia = 10
mes = 01
ano = 2000
data1 = '{}/{}/{}'.format(dia, mes, ano)
print(data1)

data2 = '{:2d}/{:2d}/{:4d}'.format(dia, mes, ano)
# A opção 'd' significa que o parâmetro é um número inteiro.
print(data2)

# Podemos forçar que os espaços em branco sejam preenchidos com o número 0:
data3 = '{:02d}/{:02d}/{:04d}'.format(dia, mes, ano)
print(data3)

# Um modo mais simples de utilizar o format
nome = "Gabriel"
profissao = "estudante"
escola = "UFABC"

print(f"{nome} é {profissao} da {escola}.")

