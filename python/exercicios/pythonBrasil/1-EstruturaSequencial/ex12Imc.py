print("Tendo como dados de entrada a altura de uma pessoa")
print("construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58")
altura = float(input("Digite sua altura ex: 1.78 "))
peso = (72.7 * altura) -58
print(f"o Peso ideal é {peso:,.1f} Kg")