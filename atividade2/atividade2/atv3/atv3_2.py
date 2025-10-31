Secreto = 8
Resposta = int(input("Digite o número secreto:"))
while Resposta != Secreto:
    if Resposta > Secreto:
        print("Muito alto! Tente um número menor.")
        Resposta = int(input("Tente adivinhar o número secreto:"))
    elif Resposta < Secreto:
        print("Muito baixo! Tente um número maior.")
        Resposta = int(input("Tente adivinhar o número secreto:"))

print("Parabéns, você acertou!")