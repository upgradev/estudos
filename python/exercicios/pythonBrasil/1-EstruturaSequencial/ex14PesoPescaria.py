print("João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o ")
print("rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o ")
print("estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar")
print("uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que")
print("leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso")
print("a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.")
print()
print("Imprima os dados do programa com as mensagens adequadas.")

MULTA = 4.0

quilos_pescado = float(input("Digite o peso total da pescaria: "))
print(f"Quantidade pescada: {quilos_pescado}")
if quilos_pescado > 50:
    excesso = quilos_pescado - 50
    multa = excesso * MULTA

    print(f"Excesso: {excesso:,.2f} Kg")
    print(f"Multa: R$ {multa:,.2f} Reais")
