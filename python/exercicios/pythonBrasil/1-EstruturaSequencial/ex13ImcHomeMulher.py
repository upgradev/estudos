print("Tendo como dado de entrada a altura (h) de uma pessoa, ")
print("construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:")
print("Para homens: (72.7*h) - 58")
print("Para mulheres: (62.1*h) - 44.7")
altura = float(input("Digite sua altura ex: 1.78 "))
sexo = input("Homem - h ou mulher - m ")
if sexo.lower() == "h":
    peso = (72.7 * altura) - 58
else:
    peso = (62.1 * altura) - 44.7

print(f"o Peso ideal é {peso:,.1f} Kg")