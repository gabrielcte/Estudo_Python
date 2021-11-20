'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/Mudanca_Tipos.py
Os dados podem vir de varias formas, é importante saber modificar seus tipo para o uso.
Segue os exercícios.
'''

# Rotina
idade = input("Informe a sua idade:")
print(idade, type(idade))

idade = int(idade)
print(idade,type(idade))

print(float("123.35"))
print(str(123.35))
print(bool(''))
print(bool(0))
print(bool('abc'))
print(bool(-2))

salario_mensal = input("Digite o valor de seu salário mensal")
salario_mensal = float(salario_mensal)

gasto_mensal = input('Digite o valor do seu gasto mensal em média:')
gasto_mensal = float(gasto_mensal)

salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12

montante_economizado = salario_total - gasto_total
print("O montate que você pode economizar ao fim do ano é", montante_economizado)
