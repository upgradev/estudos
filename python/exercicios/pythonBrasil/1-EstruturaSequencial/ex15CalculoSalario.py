print("Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.") 
print("Calcule e mostre o total do seu salário no referido mês, ")
print("sabendo-se que são descontados 11% para o Imposto de Renda,") 
print("8% para o INSS e 5% para o sindicato, faça um programa que nos dê:")
print("salário bruto.")
print("quanto pagou ao INSS.")
print("quanto pagou ao sindicato.")
print("o salário líquido.")

valor_por_hora = float(input("Qual o valor do trabalho por hora: "))
horas_trabalhadas =  float(input("Horas Trabalhadas: "))
salario_bruto = horas_trabalhadas * valor_por_hora
print(f"Salário bruto: {salario_bruto}")
imposto_renda = (11 * salario_bruto) / 100
print(f"-Imposto de renda: {imposto_renda}") 
inss = (8 * salario_bruto) / 100
print(f"-INSS: {inss}")
sindicato = (5 * salario_bruto) / 100
print(f"-Imposto de renda: {sindicato}")  
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
print(f"=Salário liquido: {salario_liquido}")