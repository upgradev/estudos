print("Faça um programa para uma loja de tintas.")
print("O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.")
print("Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a ")
print("tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a")
print("quantidades de latas de tinta a serem compradas e o preço total.")
print()
import math
metros_quadrados = float(input("Digite o valor do metro quadrado: "))
quantidade_tinta = metros_quadrados / 3
valor_lata = 18.0
if quantidade_tinta <= 18:
    print(f"Latas de tinta: {1}")
    print(f"Valor: {valor_lata}")
else:
    total_lata = math.ceil(quantidade_tinta / 18)
    valor_total_lata = total_lata * 18
    print(f"Latas de tinta: {total_lata:,.2f}")
    print(f"Valor: {valor_total_lata}")