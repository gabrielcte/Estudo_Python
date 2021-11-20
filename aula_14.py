def calcula_media(*args,margem):
    soma = sum(args)
    media = soma/len(args)
    return media + margem

def print_info(**kwargs):
    print(kwargs,type(kwargs))

print(calcula_media(10,8,9, margem=0.3))
print(print_info(nome = 'Pietro', sobrenome = 'Ribeiro'))
