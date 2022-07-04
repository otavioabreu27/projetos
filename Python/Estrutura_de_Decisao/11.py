salario = float(input())

if salario <= 280 :
    print('O salario antes do reajuste é:',salario,'R$.')
    print('O reajuste é de 20%, totalizando:',salario*0.2,'R$.')
    salario *= 1.2
elif salario > 280 and salario <= 700:
    print('O salario antes do reajuste é:',salario)
    print('O reajuste é de 15%, totalizando:',salario*0.15,'R$.')
    salario *= 1.15
elif salario > 700 and salario <= 1500:
    print('O salario antes do reajuste é:',salario)
    print('O reajuste é de 10%, totalizando:',salario*0.1,'R$.')
    salario *= 1.1
elif salario > 1500:
    print('O salario antes do reajuste é:',salario)
    print('O reajuste é de 5%, totalizando:',salario*0.05,'R$.')
    salario *= 1.05
print('Novo salario:',salario,'R$')