print("Faça um programa para a leitura de duas notas parciais de um aluno.")
print(" O programa deve calcular a média alcançada por aluno e apresentar:")
print("A mensagem Aprovado, se a média alcançada for maior ou igual a sete;")
print("A mensagem Reprovado, se a média for menor do que sete;")
print("A mensagem Aprovado com Distinção, se a média for igual a dez")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
media = (nota1 + nota2) / 2
print(f"Média: {media}")
if media >= 7.0 and media <= 9.9:
    print("Aprovado")
elif media < 7.0:
    print("Reprovado")
else:
    print("Aprovado com Distinção")
