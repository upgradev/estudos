print("Faça um Programa que peça dois números e imprima o maior deles.")
print()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O maior número é {num1} ")
elif num1 == num2:
    print(f"números iguais ")
else:
    print(f"O maior número é {num2} ")
