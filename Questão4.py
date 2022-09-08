n1 = int(input('DIgite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))
media = (n1 + n2) / 2
if media > 4:
    print(f'as suas notas foram {n1} e {n2}, a sua média foi {media}, o seu conceito foi E')
    print('REPROVADO')
elif media > 6:
    print(f'as suas notas foram {n1} e{n2}, a sua média foi {media}, o seu conceito foi D')
    print('REPROVADO')
elif media > 7.5:
    print(f'as suas notas foram {n1} e{n2}, a sua média foi {media}, o seu conceito foi C')
    print('APROVADO')
elif media > 9 :
    print(f'as suas notas foram {n1} e{n2}, a sua média foi {media}, o seu conceito foi B')
    print('APROVADO')
else:
    print(f'as suas notas foram {n1} e {n2}, a sua média foi {media}, o seu conceito foi A')
    print('APROVADO')