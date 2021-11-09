print("Faça um Programa que verifique se uma letra digitada é vogal ou consoante.")

letra = input("Digite a letra: ")
if letra.upper() == "A" or letra.upper() == "E" or letra.upper() == "I" or letra.upper() == "O" or letra.upper() == "U":
    print("Vogal")
else:
    print("Consoante")
