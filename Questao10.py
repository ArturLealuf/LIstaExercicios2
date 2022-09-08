n1 = int(input('DIgite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))
n3 = int(input('Digite sua terceira nota: '))
media = (n1 + n2 + n3) / 2
if media < 7:
    print('Reprovado.   Média final : {media}')
elif media >= 7:
    print('Aprovado.   Média final : {media}')
elif media == 10:
    print('Aprovado com distinção')
