dias = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
dia = int(input('Digite um número entre 1-7: '))
if dia > 7 or dia <= 0:
    print('não existe dia corrrespondente a este número')
else:
    dia = dia- 1
    print(dias[dia])