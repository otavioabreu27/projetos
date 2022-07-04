import math

area = float(input('Tamanho em metros quadrados da area a ser pintada:'))
print('______________________________________________________________________')

litros = float(area / 6)
latas = math.ceil(litros/18)
galao = math.ceil(litros/3.6)
cont_lata = 0
cont_galao = 0 

print('Comprando somente latas [Qtd:',latas,'] [Preco:',latas*80,'R$]')
print('Comprando somente galoes [Qtd:',galao,'] [Preco:',galao*25,'R$]')
print('______________________________________________________________________')

while litros*1.1 > 0:
    if litros >= 18:
        cont_lata+=1
        litros-=18
    else:
        cont_galao+=1
        litros-=3.6

print('A combinação com menos desperdício seria:\n')
print('[',cont_lata,'] Latas de tinta, totalizando [',cont_lata*80,'R$]')
print('[',cont_galao,'] Galoes de tinta, totalizando [',cont_galao*25,'R$]')
print('Total [',(cont_lata*80)+(cont_galao*25),'R$]')