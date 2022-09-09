valor = int(input('qual o valor da sua hora trabalhada: '))
horas = int(input('quantas horas você trabalha no mês: '))
salariob = valor * horas
desconto = 0
if salariob <= 900: desconto = 0
elif salariob <= 1500: desconto = 5/100
elif salariob <= 2500: desconto = 10/100
else: desconto = 20/100
IR = salariob * desconto
INSS = salariob * (10/100)
print(f'salario bruto = {valor} * {horas} = {valor * horas}')
print(' (-)IR (5%): R$', IR)
print(' (-)INSS (10%) : R$', INSS)
print('FGTS (11%) : R$', salariob * (11/100))
print('total de descontos : R$ ', IR + INSS)
print('salário liquido : R$  ', salariob - IR - INSS)
