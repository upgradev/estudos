print("Faça um Programa que verifique se uma letra digitada é 'F' ou 'M'.")
print(" Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.")
print()
letra = input("Digite a letra: ")
if letra.upper() == 'F':
    print("Feminino")
elif letra.upper() == "M":
    print("Masculino")
else:
    print("Sexo inválido")