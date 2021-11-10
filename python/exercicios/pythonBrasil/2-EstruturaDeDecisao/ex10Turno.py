print("Faça um Programa que pergunte em que turno você estuda.")
print("Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem Bom Dia!, Boa Tarde! ou Boa Noite! ou Valor Inválido! ")

pergunta = input(
    "Qual turno estuda? M-matutino ou V-Vespertino ou N- Noturno? ")

if pergunta.upper() == "M":
    print("Matutino")
elif pergunta.upper() == "V":
    print("Vespertino")
elif pergunta.upper() == "N":
    print("Noturno")
else:
    print("Valor Invalido")
