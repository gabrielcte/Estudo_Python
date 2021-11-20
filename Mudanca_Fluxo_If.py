'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Mudanca_Fluxo_If.py
O if ramifica o código, muito util para condicionamento da rotina. Segue os
exercícios.
'''

# Rotina
valor_passagem = 4.40
valor_corrida = input("Qual é o valor da corrida ?")
if float(valor_corrida) <= valor_passagem*5:
    print('Pague a corrida')
if float(valor_corrida) > valor_passagem*5:
    print("Pegue o onibus")
##
if float(valor_corrida) <= valor_passagem*5:
    print('Pague a corrida')
else:
    print("Pegue o onibus")
##
if float(valor_corrida) <= valor_passagem*5:
    print('Pague a corrida')
else:
    if float(valor_corrida)<=valor_passagem*6:
        print("Aguarde um momento o valor pode abaixar")
    else:
        print("Pegue o onibus")
##
if float(valor_corrida) <= valor_passagem*5:
    print('Pague a corrida')
elif float(valor_corrida)<=valor_passagem*6:
    print("Aguarde um momento o valor pode abaixar")
else:
    print("Pegue o onibus")
