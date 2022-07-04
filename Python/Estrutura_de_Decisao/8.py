print('Digite o preco de 3 produtos')
preco_1 = input()
preco_2 = input()
preco_3 = input()

if preco_1 < preco_2 and preco_1 < preco_3:
    print('Primeiro')
elif preco_2 < preco_1 and preco_2 < preco_3:
    print('Segundo')
elif preco_3 < preco_1 and preco_3 < preco_2:
    print('Terceiro')
elif preco_1 == preco_2 and preco_1 < preco_3:
    print('Primeiro ou segundo')
elif preco_1 < preco_2 and preco_1 == preco_3:
    print('Primeiro ou terceiro')
elif preco_1 > preco_2 and preco_2 == preco_3:
    print('Segundo ou terceiro')
