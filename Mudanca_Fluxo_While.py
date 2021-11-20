'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Mudanca_Fluxo_While.py
O While é um loop dentro do código, útil para preencher/modificar/contabilizar... vetores e listas, e fazer calculos repetitivos.
Segue os exércicios:
'''

# Rotina
contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "Item limpo")
    else:
        print(contador, "Itens limpos")
print('Fim da repetição do bloco while')
##
contador = 0
while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "Item limpo")
        else:
            print(contador, "Itens limpos")
    else:
        break
print('Fim da repetição do bloco while')
texto = input('Digite a sua senha: ')
##
contador = 0
while texto != 'LetsCode':
    texto = input('Senha invalida: ')
print("Acesso permitido")

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    else:
        print(contador, "Itens limpos")
print('Fim da repetição do bloco while')
##
