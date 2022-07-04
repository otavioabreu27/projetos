print('Digite 3 números')
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())

#usando o exit pra que numeros iguais nao se repitam
if num_1 >= num_2 and num_1 >= num_3:
    print(num_1)
    exit()
elif num_2 >= num_1 and num_2 >= num_3:
    print(num_2)
    exit()
elif num_3 >= num_2 and num_3 >= num_2:
    print(num_3)
    exit()