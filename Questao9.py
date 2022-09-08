num = int(input('Digite um número inteiro menor que 1000: '))
numinicial = num
if num > 999:
    print('Número invalido')
unidade = num % 10
num = (num - unidade)/10
dezena = num % 10
num = (num - dezena)/10
centena = num
dezena = int(dezena)
centena = int(centena)
cs = "centenas"
ds = "dezenas"
us = "unidades"
if unidade == 1: us = "unidade"
if dezena == 1: ds = "dezena"
if centena == 1: cs = "centena"
if num < 100:
    print(f'{numinicial} = {dezena} {ds} e {unidade} {us}')    
if num < 10:
    print(f'{numinicial} = {unidade} {us}')
else:
    print(f'{numinicial} = {centena} {cs}, {dezena} {ds} e {unidade} {us}')
