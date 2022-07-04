import math

#função que gera o numero de latas arredondado pra cima (não da pra comprar meia lata)
def qtd_latas (area):  
    return int(math.ceil(area/54))

metros_quad = float(input('Qual o tamanho em metros quadrados a ser pintado?\n'))

print('Você precisará de',qtd_latas(metros_quad),'latas, totalizando',80*qtd_latas(metros_quad),'R$.')