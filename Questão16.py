litros = int(input('quantos litros foram vendidos? '))
combustivel = input("qual foi o combustivel vendido: \na = alcool \ng = gasolina \n")
while combustivel != 'g' and 'a':
    print('código invalido')
    combustivel = input("qual foi o combustivel vendido: \na = alcool \ng = gasolina \n")
if combustivel == 'g':
    preço = 2.50
elif combustivel == 'a':
    preço = 1.90
if combustivel == 'g' and litros > 20:
    desconto = 6/100
elif combustivel == 'g' and litros <= 20:
    desconto = 4/100
elif combustivel == 'a' and litros > 20:
    desconto = 5/100
else: desconto: 3/100
preço2 = litros * preço
preço_final = preço2 - (preço2 * desconto)
print(f'o valor final será de {preço_final}')
