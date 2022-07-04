peso = int(input('Digite o peso:\n'))

#teste condicional para checar se há irregularidade
if peso > 50:
    excesso = peso-50
    multa = excesso*4.00
    print('Foram pesados',excesso,'kg de excesso e portanto a multa é de',multa,'R$')
else:
    print('Não há irregularidades!')
