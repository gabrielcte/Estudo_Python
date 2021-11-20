'''
Gabriel Alves Silva
https://github.com/gabrielcte/Estudo_Python/blob/main/lendo_escrevendo_txt.py
Como abrir e utilizar um documento txt com o Python, segue o exercício.
'''

# Rotina
arquivo = open('dom_casmurro_cap_1.txt', 'r')
texto = arquivo.read()
print(texto)
arquivo.close()

arquivo = open('dom_casmurro_cap_1.txt', 'r')
linha = arquivo.readline()
while linha != '':
    print(linha,end='')
    linha = arquivo.readline()
arquivo.close()

arquivo = open('dom_casmurro_cap_1.txt', 'r')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

with open('dom_casmurro_cap_1.txt', 'r') as arquivo:
    texto =arquivo.read()
    print(texto)

with open('arquivo_teste.txt', 'w',) as arquivo:
    arquivo.write('Essa é uma linha que eu escrevi usando Python\n')
    arquivo.write('Essa é a segunda linha linha que eu escrevi usando Python\n')

with open('arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')

with open('arquivo_teste.txt', 'a',) as arquivo:
    arquivo.write('Essa é a terceira linha que eu escrevi usando Python\n')

with open('arquivo_teste.txt', 'r') as arquivo:
    print(arquivo.read(), end='')
