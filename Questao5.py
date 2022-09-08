a = int(input("Lado A: "))
b = int(input("Lado B: "))
c = int(input("Lado C: "))
if a <= 0 or b <= 0 or c <= 0:
    print("Valor invalido em um dos lados!")
elif a + b > c and a + c > b and b + c > a:
    print("formou um triangulo")
    if a == b and b == c:
        print("Triangulo Equilatero")
    elif a != b and b != c and a != c:
        print("Triangulo Escaleno")
    elif a == b or a == c or b == c:
        print("Triangulo Isosceles")
    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
        print("Triangulo Retangulo")
else:
    print("Nao forma um Triangulo!")
