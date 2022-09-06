salario = int(input('digite o seu salário: '))
novo_salario = 0
porcentagem = 0
if salario < 281:
    porcentagem = 20/100
    novo_salario = salario + (salario * porcentagem)
elif salario < 700:
    porcentagem = 15/100
    novo_salario = salario + (salario * porcentagem)
elif salario < 1500: 
    porcentagem = 10/100
    novo_salario = salario + (salario * porcentagem)
else: 
    porcentagem = 5/100
    novo_salario = salario + (salario * porcentagem)
aumento = novo_salario - salario
print(f'O seu salário era de {salario} R$')
print(f'Seu salario foi aumentado em {porcentagem * 100}%')
print(f'Seu aumento foi de {aumento} R$')
print(f'E seu novo salário é {novo_salario}R$')
