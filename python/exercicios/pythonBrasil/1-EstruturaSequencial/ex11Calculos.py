print("Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:")
print("o produto do dobro do primeiro com metade do segundo .")
print("a soma do triplo do primeiro com o terceiro.")
print("o terceiro elevado ao cubo.")

num1 = int(input("Digite o primeiro inteiro: "))
num2 = int(input("Digite o segundo inteiro: "))
num3 = float(input("Digite o número real: "))

dobro_primeiro = num1 * num1
metade_segundo = num2 // 2
triplo_primeiro = num1 * num1 * num1
terceiro_cubo = num3 ** 3

res1 = dobro_primeiro * metade_segundo
res2 = triplo_primeiro + num3
res3 = terceiro_cubo

print(f"o produto do dobro do primeiro com metade do segundo: {res1}")
print(f"a soma do triplo do primeiro com o terceiro: {res2} ")
print(f"o terceiro elevado ao cubo: {res3:,.2f}")

