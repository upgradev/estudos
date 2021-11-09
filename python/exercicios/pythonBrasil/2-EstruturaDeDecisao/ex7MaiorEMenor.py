print("Faça um Programa que leia três números e mostre o maior e o menor deles.")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2:
    if num1 > num3:
        print(f"Maior {num1}")
        if num2 > num3:
            print(f"Menor: {num3}")
        else:
            print(f"Menor: {num2}")

    else:
        print(f"Maior {num3}")
        if num1 > num2:
            print(f"Menor: {num2}")
        else:
            print(f"Menor: {num1}")


elif num1 > num3:
    if num1 > num2:
        print(f"Maior {num1}")
        if num2 > num3:
            print(f"Menor: {num3}")
        else:
            print(f"Menor: {num2}")
    else:
        print(f"Maior {num2}")
        if num1 > num3:
            print(f"Menor: {num3}")
        else:
            print(f"Menor: {num1}")

else:
    if num2 > num3:
        print(f"Maior {num2}")
        if num1 > num3:
            print(f"Menor: {num3}")
        else:
            print(f"Menor: {num1}")
    else:
        print(f"Maior {num3}")
        if num2 > num1:
            print(f"Menor: {num1}")
        else:
            print(f"Menor: {num2}")
