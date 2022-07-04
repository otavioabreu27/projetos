from ast import Break, Return

#função com tratador de excessão que indica se o nº é inteiro
def is_int(inteiro):
    try:    
        int(inteiro)
        return True
    except ValueError:
        return False

inteiro_1 = input('Digite um numero inteiro: ')

#loop que impede o usuário de continuar caso o nº não seja inteiro
while is_int(inteiro_1) != True:
    inteiro_1 = input('Digite novamente: ')

inteiro_2 = input('Digite outro numero inteiro:')

#loop que impede o usuário de continuar caso o nº não seja inteiro
while is_int(inteiro_2) != True:
    inteiro_2 = input('Digite novamente: ')

real = float(input('Digite um numero real: '))

print('A =',(int(inteiro_1)*2)*int(inteiro_2)/2)
print('B =',(int(inteiro_1)*3)+real)
print('C =', real**3)
