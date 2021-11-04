# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print("Programa que peça as 4 notas bimestrais e mostre a média")
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))
num4 = float(input("Digite a quarta nota: "))

media = (num1 + num2 + num3 + num4) / 4
print(f"A média é: {media:,.1f}")