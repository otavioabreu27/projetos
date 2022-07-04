print('Digite as medias')
med_1 = float(input())
med_2 = float(input())

if (med_1 + med_2)/2 >= 7 and (med_1 + med_2)/2 != 10:
    print('Aprovado')
elif (med_1 + med_2)/2 < 7:
    print('Reprovado')
elif (med_1 + med_2)/2 == 10:
    print('Aprovado com distinção')