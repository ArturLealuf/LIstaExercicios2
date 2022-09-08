a = float(input('Digite um número: '))
b = float(input('Digite outro número: '))
print(' digite "+" para somar \n digite "-" para subtrair \n digite "*" para multiplicar \n digite "/" para dividir')
operador = input('Digite sua opção: ')
if operador == '+':
    resultado = a+b
elif operador == '-':
    resultado = a-b
elif operador == '*':
    resultado = a*b
elif operador == '/':
    resultado = a/b
else:
    print('opção não disponivel')
if resultado % 2 == 0:
    iop = 'é par'
else: iop = 'não é par'
if resultado == round(resultado):
    decima = 'não é decimal'
else:
    decima = 'é decimal'
if resultado >=0:
    mom = 'positivo'
else: mom = 'negativo'
print(f'o resultado da operação foi: {resultado}!  \neste número {iop}, é {mom}, e {decima}')

