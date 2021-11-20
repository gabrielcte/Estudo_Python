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