res1 = int(input("Telefonou para a vítima? 1=Sim ou 0=Não: "))
res2 = int(input("Esteve no local do crime? 1=Sim ou 0=Não: "))
res3 = int(input("Mora perto da vítima? 1=Sim ou 0=Não: "))
res4 = int(input("Devia para a vítima? 1=Sim ou 0=Não: "))
res5 = int(input("Já trabalhou com a vítima? 1=Sim ou 0=Não: "))
soma_respostas = res1 + res2 + res3 + res4 + res5
if (soma_respostas < 2):
 print("Inocente")
elif (soma_respostas == 2):
 print("Suspeita")
elif (3 <= soma_respostas <= 4):
 print("Cúmplice")
elif (soma_respostas == 5):
 print("Assassino")
