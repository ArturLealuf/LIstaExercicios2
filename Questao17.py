kg_maca = int(input('Quantos kilos de maçã foram comprados? '))
kg_mor = int(input('Quantos kilos de morango foram comprados? '))
if kg_maca > 5:
    preço_maca = 1.50
else: 
    preço_maca = 1.80
if kg_mor > 5:
    preço_mor = 2.20
else:
    preço_mor = 2.50
pfma = kg_maca * preço_maca
pfmo = kg_mor * preço_mor
preço_final = pfma + pfmo
if kg_mor + kg_maca > 8 or preço_final > 25:
    preço_final = preço_final - (preço_final * 10 /100)
print(f'o valor final a ser pego é de {preço_final} R$')
