hora = float(input('Quanto voce ganha por hora?\n'))
qtd_hora = float(input('Quantas horas voce trabalhou esse mes?\n'))
salario = hora*qtd_hora
print('+ Salario bruto = R$',salario)
print('- IR (11%) = R$',salario*0.11)
print('- INSS (8%) = R$',salario*0.08)
print('- Sindicato (5%) = R$',salario*0.05)
print('= Salário Liquido : R$',salario-((salario*0.11)+(salario*0.08)+(salario*0.05)))